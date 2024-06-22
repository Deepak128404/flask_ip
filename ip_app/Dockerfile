FROM python:3.9 AS builder

# Set the working directory
WORKDIR /app

# Copy the entire repository content into the container
COPY . .

# List the contents to debug
RUN ls -R

# Install dependencies
RUN pip install -r /app/ip_app/requirements.txt

# Second stage
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy files from the builder stage
COPY --from=builder /app /app
COPY --from=builder /usr/local /usr/local

# List the contents to debug
RUN ls -R

# Expose the port the app runs on
EXPOSE 5000

# Set the entry point
ENTRYPOINT ["python"]

# Set the command
CMD ["/app/ip_app/get_container_ip.py"]
