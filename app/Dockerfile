# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

COPY . /app

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "main.py", "--host", "0.0.0.0:5000" ]
