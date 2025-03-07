#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Lambda code that pulls tweets in and saves them to s3 and to a DB
"""

from newsapi import NewsApiClient
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer

from dateutil import parser
from datetime import datetime
import logging
import json
import os
import pytz
from typing import Optional


from botocore.exceptions import ClientError
import boto3
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import psycopg2
import psycopg2.extras

try:
    sia = SentimentIntensityAnalyzer()
except LookupError:
    import nltk
    # in lambda you can only write to /tmp folder
    # nltk needs to download data to run a model
    nltk.download('vader_lexicon', download_dir='/tmp')
    # nltk will look for the downloaded data to run SentimentIntensityAnalyzer
    nltk.data.path.append("/tmp")
    sia = SentimentIntensityAnalyzer()

def _get_sentiment(string: str) -> float:
    '''
    make sure the score is between -1 (very negative) and 1 (very positive)
    '''
    # sia is the SentimentIntensityAnalyzer object which gives a positive and negative score
    score = sia.polarity_scores(string)
    # we want only 1 score so the negative sentiment will be a negative score 
    # and likewise for the positive
    score = score['neg'] * -1 + score['pos']
    return score

def add_sentiment_score(news: dict) -> dict:
    news['sentiment_score'] = _get_sentiment(news['description'])
    return news


from datetime import datetime
curr_dt = datetime.now()

def convert_timestamp_to_int(news: dict) ->dict:
    '''datetime object are not serializable for json,
    so we need to convert them to unix timestamp'''
    #now_str = round(curr_dt.timestamp())
    now_str = datetime.now(tz=pytz.UTC).strftime('%d-%m-%Y-%H:%M:%S')
    #print(type(now_str))
    news = news.copy()
    news['timestamp'] = now_str
    return news

def upload_file_to_s3(local_file_name: str,
                      bucket: str,
                      s3_object_name: Optional[str]=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param s3_object_name: If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if s3_object_name is None:
        s3_object_name = local_file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(local_file_name, bucket, s3_object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def get_db_connection() -> psycopg2.extensions.connection:
    # to connect to DB, use the parameters and password that define it
    conn = psycopg2.connect(
                            user="postgres",
                            password=os.environ['DB_PASSWORD'],
                            host=os.environ['DB_HOST'],
                            port="5432",
                            connect_timeout=1)
    return conn


def insert_data_in_db(df: pd.DataFrame,
                      conn: psycopg2.extensions.connection,
                      table_name: str = 'tweets_analytics') -> None:
    # you need data and a valid connection to insert data in DB
    are_data = len(df) > 0
    if are_data and conn is not None:
        try:
            cur = conn.cursor()
            # to perform a batch insert we need to reshape the data in 2 strings with the column names and their values
            df_columns = list(df.columns)
            columns = ",".join(df_columns)

            # create VALUES('%s', '%s",...) one '%s' per column
            values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))

            # create INSERT INTO table (columns) VALUES('%s',...)
            # here the final 2 strings are created
            insert_string = "INSERT INTO {} ({}) {}"
            insert_stmt = insert_string.format(table_name, columns, values)
            psycopg2.extras.execute_batch(cur, insert_stmt, df.values)
            conn.commit()
            print('succesful update')

        except psycopg2.errors.InFailedSqlTransaction:
            # if the transaction fails, rollback to avoid DB lock problems
            logging.exception('FAILED transaction')
            cur.execute("ROLLBACK")
            conn.commit()

        except Exception as e:
            # if the transaction fails, rollback to avoid DB lock problems
            logging.exception(f'FAILED  {str(e)}')
            cur.execute("ROLLBACK")
            conn.commit()
        finally:
            # close the DB connection after this
            cur.close()
            conn.close()
    elif conn is None:
        raise ValueError('Connection to DB must be alive!')
    elif len(df) == 0:
        raise ValueError('df has 0 rows!')



def lambda_handler(event, context):
    try:
        # wrap the body into a try/catch to avoid lambda automatically re-trying

        # take the environment variables
        S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
        newsapi = NewsApiClient(api_key='6f57b1e93a12438ab58a13cf601dce07')
        all_articles = newsapi.get_everything(q='war',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2024-06-01',
                                      to='2024-06-11',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
        
        # we decided to follow reuters. You can put something else too =)
        recent_news= [{'author':all_articles['articles'][news]['author'], 
               'description':all_articles['articles'][news]['description']} 
              for news in range(len(all_articles['articles']))]

        sentiment = [add_sentiment_score(news) for news in recent_news]

        now_str = datetime.now(tz=pytz.UTC).strftime('%d-%m-%Y-%H:%M:%S')
        filename = f'{now_str}.json'
        output_path_file = f'/tmp/{filename}'
        print(now_str)
        #in lambda files need to be dumped into /tmp folder
        with open(output_path_file, 'w') as fout:
            news_to_save = [convert_timestamp_to_int(news)
                                for news in sentiment]
            json.dump(news_to_save , fout)

        #print(news_to_save)
        news_df = pd.DataFrame(news_to_save)
        #news_df.to_csv('news_sentiment.csv',index=False)
        upload_file_to_s3(local_file_name=output_path_file,
                          bucket=S3_BUCKET_NAME,
                          s3_object_name=f'raw-messages/{filename}')

        news_df = pd.DataFrame(news_to_save)
        conn = get_db_connection()
        insert_data_in_db(df=news_df, conn=conn, table_name='newss_analytics')
    except Exception as e:
        logging.exception('Exception occured \n')
    # add_messages_to_db(df=tweets_df, conn=conn)
    print('Lambda executed succesfully!')


if _name_ == "_main_":
    lambda_handler({}, {}) # type: ignore


# create_table.py
from db import get_db_connection

def create_users_table():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Define the CREATE TABLE query
            create_table_query = """
            CREATE TABLE IF NOT EXISTS news (
                id SERIAL PRIMARY KEY,
                timestamp varchar(20),
                author VARCHAR(50),
                sentiments_score FLOAT,
                Description varchar(700)
            );
            """
            cursor.execute(create_table_query)
            conn.commit()
            cursor.close()
            print("news table created successfully or already exists.")
        except Exception as e:
            print(f"Error creating news table: {e}")
        finally:
            conn.close()


# crud/create.py
from db import get_db_connection

def create_user(id, timestamp,  author, sentiments_score, description):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO news (id, timestamp,  author, sentiments_score, description) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(query, (id, timestamp,  author, sentiments_score, description))
            conn.commit()
            cursor.close()
            print(f"User: {id} created successfully.")
        except Exception as e:
            print(f"Error creating user: {e}")
        finally:
            conn.close()

#news-fetch
import requests
import pandas as pd
from textblob import TextBlob

# API Key and Endpoint
API_KEY = "fd7c2acb582944198c6fa55efcf26393"  
URL = f"https://newsapi.org/v2/everything?q=tesla&from=2024-12-17&sortBy=publishedAt&apiKey={API_KEY}"

def fetch_news_data():
    """
    Fetch news data from the News API and process it.
    """
    try:
        # Make a request to the News API
        response = requests.get(URL)
        if response.status_code != 200:
            print(f"Error fetching data: HTTP {response.status_code}")
            return None

        # Parse the response JSON
        news_data = response.json()
        articles = news_data.get("articles", [])
        if not articles:
            print("No articles found in the response.")
            return None

        # Process the articles and calculate sentiment
        table_data = []
        for article in articles:
            timestamp = article.get("publishedAt")
            author = article.get("author")
            description = article.get("description")
            sentiment_score = TextBlob(description).sentiment.polarity if description else 0.0

            table_data.append({
                "timestamp": timestamp,
                "author": author,
                "sentiment_score": sentiment_score,
                "description": description
            })

        # Convert to DataFrame
        return pd.DataFrame(table_data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to fetch and display news data.
    """
    print("Fetching news data...")
    news_df = fetch_news_data()

    if news_df is not None and not news_df.empty:
        print("\nTop 5 News Articles:\n")
        print(news_df.head())  # Display the first 5 rows
        print("\nFull DataFrame saved to 'news_data.json'.")
        news_df.to_json("news_data.json", index=False)  # Save to a CSV file
    else:
        print("No data available.")

if __name__ == "__main__":
    main()