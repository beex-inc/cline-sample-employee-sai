# FROM python:3.11-slim
FROM python:3.9-slim

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    chromium \
    fonts-ipafont-gothic fonts-ipafont-mincho \
    git \
    curl \
    default-libmysqlclient-dev \
    default-mysql-client \
    pkg-config \
    build-essential \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# AWS CLIのインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf aws awscliv2.zip

# 作業ディレクトリの設定
WORKDIR /workspace

# vscodeユーザーの作成
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Python環境の設定
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Set environment variables for Chrome
ENV CHROME_PATH=/usr/bin/chromium

# 必要なPythonパッケージのインストール
RUN pip install --no-cache-dir \
    black \
    pylint \
    pytest

USER $USERNAME
