# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy your Flask API code and trained model file into the container
COPY heart_ml.py heartDiseaseMlUpdated.pkl ./

# Install Flask and any other required dependencies
RUN pip install Flask==2.0.1 Flask-Cors scikit-learn 

# Expose the port the app runs on
EXPOSE 4000

# Define the command to run your Flask app
CMD ["python", "heart_ml.py"]
