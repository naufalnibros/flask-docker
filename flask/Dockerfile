FROM python:3

RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app

EXPOSE 5000

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY / .
RUN ls -l 

CMD [ "uwsgi", "--ini", "flask/app.ini" ]