FROM mcr.microsoft.com/devcontainers/python:3.11

# Avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install core dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    gnupg \
    apt-transport-https \
    lsb-release

# --- Install Google Cloud CLI ---
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list && \
    apt-get update && apt-get install -y google-cloud-cli

# --- Install Node.js (needed for Gemini CLI) ---
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs

# --- AWS CLI (If you still need it for Bedrock) ---
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    apt-get install -y unzip && unzip awscliv2.zip && ./aws/install && rm -rf awscliv2.zip aws