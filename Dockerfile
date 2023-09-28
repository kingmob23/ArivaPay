FROM python:latest

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w 4 'main:app'"]