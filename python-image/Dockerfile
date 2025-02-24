# FROM python:3.9-slim
# WORKDIR /app
# RUN pip install --no-cache-dir streamlit sqlalchemy pandas textblob psycopg2-binary
# COPY . /app
# EXPOSE 8501
# CMD ["streamlit", "run", "app.py","--server.port=8501","server.enableCORS=false"]

# Use official slim Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies for psycopg2-binary
RUN apt-get update && apt-get install -y gcc libpq-dev

# Install Python packages
RUN pip install --no-cache-dir streamlit sqlalchemy pandas textblob psycopg2-binary

# Copy project files
COPY . .

# Expose port for Streamlit
EXPOSE 8051

# Start Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8051", "--server.enableCORS=false"]
