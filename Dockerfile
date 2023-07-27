# Use a base image with Python 3 and other required dependencies
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy all files from the root directory to the working directory in the container
COPY . /app

# Install Python dependencies from requirements.txt

RUN pip install -r requirements.txt

RUN chmod +x /app/run.sh
# Run shinyapp
CMD ["bash", "-c", "/app/run.sh"]