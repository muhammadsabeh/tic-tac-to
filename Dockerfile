FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1

CMD ["python", "app.py"]