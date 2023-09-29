FROM python:latest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w 4", "--bind", "0.0.0.0:8000", "main:app"]