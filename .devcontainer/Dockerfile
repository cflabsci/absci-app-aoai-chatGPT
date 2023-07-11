ARG IMAGE=bullseye
FROM --platform=amd64 mcr.microsoft.com/devcontainers/${IMAGE}
RUN export DEBIAN_FRONTEND=noninteractive \
     && apt-get update && apt-get install -y xdg-utils \
     && apt-get clean -y && rm -rf /var/lib/apt/lists/*
     && ACCEPT_EULA=Y apt-get install -y msodbcsql18
     && ACCEPT_EULA=Y apt-get install -y mssql-tools18
     && apt-get install -y unixodbc-dev
RUN curl -fsSL https://aka.ms/install-azd.sh | bash
