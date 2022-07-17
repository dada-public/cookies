FROM python:3.8-slim

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Normalize python version
RUN ln -s /usr/bin/python3 /usr/bin/python

# Container dependencies. Sage Maker operates the container through an API
RUN pip3 --no-cache-dir install flask gevent gunicorn

# Our own set of dependencies
COPY src/algorithm/requirements.txt /tmp/requirements.txt
RUN pip3 --no-cache-dir install -r /tmp/requirements.txt

# Keep python buffering logs
ENV PYTHONUNBUFFERED=TRUE
# Avoid unnecessary .pyc files
ENV PYTHONDONTWRITEBYTECODE=TRUE
# Set path so SageMaker knows where to invoke our server
ENV PATH="/opt/program:${PATH}"

COPY src /opt/program
WORKDIR /opt/program
