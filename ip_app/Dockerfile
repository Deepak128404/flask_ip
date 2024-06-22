FROM python AS builder

WORKDIR /app

ADD https://github.com/Deepak128404/flask_ip.git .
# Copy requirements file locally
COPY requirements.txt /tmp/requirements.txt

# Install dependencies in the builder stage
RUN pip install -r /tmp/requirements.txt

# Second stage
FROM python:3.9-slim
WORKDIR /app

# Copy files from the builder stage
COPY --from=builder /app /app
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib /usr/local/lib

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["ip_app/get_container_ip.py"]
