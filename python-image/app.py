import psycopg2
import streamlit as st
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(page_title="News Analytics Dashboard", layout="wide")

# Database connection settings
DB_SETTINGS = {
    "host": "db-postgres-sandra.cz48w48q6q3w.ap-south-1.rds.amazonaws.com",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "postgresroot",
}

# Function to fetch data from PostgreSQL
@st.cache_data
def fetch_data():
    try:
        # Establish connection
        connection = psycopg2.connect(**DB_SETTINGS)
        cursor = connection.cursor()
        
        # Execute query
        query = "SELECT * FROM news;"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Fetch column names
        column_names = [desc[0] for desc in cursor.description]
        
        # Convert to DataFrame
        data = pd.DataFrame(rows, columns=column_names)
        
        # Close connection
        cursor.close()
        connection.close()
        
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if an error occurs

# Function to apply sentiment-based coloring
def apply_sentiment_color(val):
    """
    Apply background color based on sentiment values.
    Positive: Green, Negative: Red, Neutral (0): Yellow.
    """
    if val > 0:
        color = "green"
    elif val < 0:
        color = "red"
    else:
        color = "yellow"
    return f"background-color: {color}; color: white;"

# Streamlit App Layout
st.title("News Analytics Dashboard")
st.write("This dashboard displays news data fetched from the PostgreSQL database.")

# Fetch and display data
with st.spinner("Loading data from the database..."):
    data = fetch_data()

if not data.empty:
    st.write("### News Data:")
    
    # Assuming there is a 'sentiment' column in the data with numerical sentiment values
    if "sentiments_score" in data.columns:
        # Style the DataFrame for sentiment
        styled_data = data.style.applymap(apply_sentiment_color, subset=["sentiments_score"])
        st.dataframe(styled_data, use_container_width=True)
    else:
        st.dataframe(data, use_container_width=True)
        st.warning("The sentiment column is not available in the data.")

    # Example visualization (update column names as per your data)
    if "sentiments_score" in data.columns:
        st.bar_chart(data["sentiments_score"])
else:
    st.warning("No data available in the news table.")