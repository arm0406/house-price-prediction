# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install pipenv
RUN pip install pipenv 

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the files
COPY . .

# Expose flask port
EXPOSE 5000

# Run flask app using pipenv
CMD ["pipenv", "run", "python", "predict.py"]
