FROM python:3.9-slim

# OS vulnerabilities fix
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .

CMD ["python", "app.py"]