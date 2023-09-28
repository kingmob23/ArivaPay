FROM python:latest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=main.py

RUN flask db init
RUN flask db migrate -m "initial migration"
RUN flask db upgrade

CMD ["gunicorn", "-w 4", "--bind", "0.0.0.0:8000", "main:app"]
