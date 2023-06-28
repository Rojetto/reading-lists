# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container to /app
WORKDIR /app

# Copy the application code into the working directory
COPY . .

# Install application dependencies
RUN npm ci

# Build the application
RUN npm run build

# Start the application
CMD [ "npm", "run", "start" ]

