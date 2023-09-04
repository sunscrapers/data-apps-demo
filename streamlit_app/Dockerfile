###############
# BUILD IMAGE #
###############
FROM python:3.9.6-slim

# Add and install requirements
RUN pip install --upgrade pip
COPY ./streamlit_app/requirements/base.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY ./streamlit_app /app
COPY ./common /app/common
WORKDIR app

# Run streamlit
CMD streamlit run app.py
