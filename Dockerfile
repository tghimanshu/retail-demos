# Use a slim Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Streamlit uses
EXPOSE 8501

ENV PROJECT_ID=learn-361304
ENV LOCATION=us-central1

# Define the command to run your Streamlit app
# Replace "your_app.py" with the name of your main Streamlit file
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
