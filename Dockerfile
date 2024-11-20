# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY ./requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . /code/

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PORT=8080

# Run the app. CMD is required to run on Heroku
# $PORT is set by Heroku            
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8080"]
