# Use the official Python image as the base image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required packages
RUN pip install -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "stream_lit.py"] 
