# Uses an official Python base image
FROM python:3.12-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# Sets the working directory in the container
WORKDIR /app

# Copies requirements files and source code to the container
COPY ./requirements.txt .

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the application source code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Default command to run your application
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]