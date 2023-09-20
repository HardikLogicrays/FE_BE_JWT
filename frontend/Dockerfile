# # Use an official lightweight Node.js runtime as the base image
# FROM node:14-slim

# # Set the working directory to /app
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install a simple HTTP server
# RUN npm install -g http-server

# # Make port 80 available to the world outside this container
# EXPOSE 5000

# # Run the HTTP server
# CMD [ "http-server", "/app", "-p", "5000" ]


# Use an official lightweight Node.js runtime as the base image
FROM node:14-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install a simple HTTP server
RUN npm install -g http-server

# Expose port 5000
EXPOSE 5000

# Run the HTTP server on port 5000
CMD [ "http-server", "/app", "-p", "5000" ]
