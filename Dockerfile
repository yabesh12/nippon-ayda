# Pull base image
FROM python:3.9.5-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Copy Req.txt
COPY requirements.txt /app/

# Install Requirements
RUN pip install -r requirements.txt

# Copy the code
COPY . /app/

# Expose Django Port
EXPOSE 8009

# Copy the entrypoint script
COPY entry.sh /entry.sh

# Fix script Permissions
RUN chmod +x /entry.sh

# Entrypoint
ENTRYPOINT ["/entry.sh"]
