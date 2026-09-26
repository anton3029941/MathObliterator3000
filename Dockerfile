FROM python:3.12
    
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["gunicorn", "--chdir", "server", "-b", "0.0.0.0:10000", "--workers", "1", "--timeout", "300", "server:app"]
