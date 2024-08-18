# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model script and any necessary files into the container
COPY . /app

# Command to run your model script
CMD ["python", "model.py"]
