FROM node:20-alpine AS frontend  
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app 
COPY ./frontend/package*.json ./  
USER node
RUN npm ci  
COPY --chown=node:node ./frontend/ ./frontend  
COPY --chown=node:node ./static/ ./static  
WORKDIR /home/node/app/frontend
RUN npm run build
  
FROM python:3.9.7-alpine3.14  
RUN apk add --no-cache --virtual .build-deps \
    build-base \  
    libffi-dev \  
    openssl-dev \  
    curl \  
    && apk add --no-cache \  
    libpq \  
    && pip install --no-cache-dir uwsgi  \
    && curl -O https://download.microsoft.com/download/1/f/f/1fffb537-26ab-4947-a46a-7a45c27f6f77/msodbcsql18_18.2.2.1-1_amd64.apk \
    && curl -O https://download.microsoft.com/download/1/f/f/1fffb537-26ab-4947-a46a-7a45c27f6f77/mssql-tools18_18.2.1.1-1_amd64.apk \
    && apk add --allow-untrusted msodbcsql18_18.2.2.1-1_amd64.apk \
    && apk add --allow-untrusted mssql-tools18_18.2.1.1-1_amd64.apk \
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt \  
    && rm -rf /root/.cache  
  
COPY . /usr/src/app/  
COPY --from=frontend /home/node/app/static  /usr/src/app/static/
WORKDIR /usr/src/app  
EXPOSE 80  
CMD ["uwsgi", "--http", ":80", "--wsgi-file", "app.py", "--callable", "app", "-b","32768"]  
