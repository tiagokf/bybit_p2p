FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Usar gunicorn para produção
RUN pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "web_app:app"]