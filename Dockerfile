FROM python:3.10

# Set working directory for the backend
WORKDIR /app

# Copy backend requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm for the front-end
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

# Set working directory for the front-end
WORKDIR /app/front

# Copy package.json first to leverage Docker cache
COPY front/package.json ./

# Install front-end dependencies
RUN npm install --verbose

# Copy the rest of the front-end code
COPY front/ .

# Build the front-end
RUN npm run build --verbose

# Set working directory back to the backend
WORKDIR /app

# Copy the backend code
COPY . .

# Command to run the FastAPI backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
