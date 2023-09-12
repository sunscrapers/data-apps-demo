###############
# BUILD IMAGE #
###############
FROM python:3.9.6-slim

# Add and install requirements
RUN pip install --upgrade pip
COPY ./dash_app/requirements/base.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY . /app
WORKDIR app

# Run Dash app
CMD python app.py
