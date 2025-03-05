# ML_ECS_pipeline
A ML containerisation project which makes use of ECS to deploy a streamlit app which can query data from postgres rds in aws which is populated using a automated labmbda function by making use of a NewsAPI
![1](https://github.com/user-attachments/assets/352289b8-7159-4b1c-a48a-33fa2471dfe6)

In this project

* We are making use of a NewsAPI where we get the latest news articles with help of a API_Key obtained from the news api website
  after creating a developer account

* News articles are extracted with the help of a lambda function which is triggered every 1 hr using Event bridge.

* The raw data extrated are pushed to a S3 bucket and stored in json format
  ![2](https://github.com/user-attachments/assets/f74dca1f-6398-4874-bfa0-54f85ddecd9d)

* Analyzed  news aritcle are pushed to a rds postgres AWS instance along with timestamp.
  ![3](https://github.com/user-attachments/assets/9bbed5e3-c7e4-49b2-ae03-cc82f75a4d16)
  ![4](https://github.com/user-attachments/assets/04d22b1a-9f22-4d4a-a139-24391e945a4a)

* Now a Dashboard is created using Streamlit to visualize the sentiment of the news in local system which is then converted to a docker image and pushed to ECR Registry in AWS.
  ![5](https://github.com/user-attachments/assets/d316565b-bfab-49b5-8a15-578fc0239379)
  ![6](https://github.com/user-attachments/assets/e5b751a3-8650-48c5-a7c3-e548ceca1206)
  ![7](https://github.com/user-attachments/assets/6c2f5cc1-f9b7-44a5-9bc9-5d2270997642)

* The uploaded image is run using a AWS Fargate cluster by create a task definition and using the publicIP and assigned port
  we can access the Streamlit Dashboard.
  ![8](https://github.com/user-attachments/assets/f486f91f-7713-4b98-b94a-74134c67caa6)
  ![9](https://github.com/user-attachments/assets/68633772-aa83-49cd-8497-698fd71bf8fd)
  ![10](https://github.com/user-attachments/assets/e6678286-7c3d-47e6-8938-9d7f4c5490b8)
