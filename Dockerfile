FROM python:3.10

# Set working directory for the backend
WORKDIR /app

# Copy backend requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY . .

# Install Node.js for the front-end
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

# Set working directory for the front-end
WORKDIR /app/front

# Install front-end dependencies and build the front-end
RUN npm install && npm run build

# Set working directory back to the backend
WORKDIR /app

# Command to run the FastAPI backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]