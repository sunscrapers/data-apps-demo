###############
# BUILD IMAGE #
###############
FROM python:3.9.6-slim

# Install Ubuntu requirements
RUN apt-get update && apt-get -y install gcc

# Add and install requirements
RUN pip install --upgrade pip
COPY ./requirements/requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . /app
WORKDIR app

# Run streamlit
CMD panel serve app.py --autoreload --show
