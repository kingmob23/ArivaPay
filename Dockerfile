FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w", "1", "--bind", "0.0.0.0:8000", "run:app"]
