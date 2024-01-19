###############
# BUILD IMAGE #
###############
FROM mcr.microsoft.com/playwright:v1.41.0-jammy

# Install Ubuntu requirements
RUN apt update && apt install -y python3-pip

# Install requirements
RUN pip install --upgrade pip
COPY ./tests/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Install playwright dependencies
RUN playwright install

# Copy project files
COPY ./tests /tests
WORKDIR tests
