# Stage 1: Build the frontend assets
FROM node:14 as frontend

# Set the working directory for the frontend
WORKDIR /app/frontend

COPY package.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of your frontend code
COPY . .

# Stage 2: Create the final Flask container
FROM python:latest

# Set the working directory for your Flask app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy only the necessary files from the frontend container
COPY --from=frontend /app/frontend /app/static
COPY . .

# Start your Flask application
CMD ["gunicorn", "-w 4", "--bind", "0.0.0.0:8000", "main:app"]
