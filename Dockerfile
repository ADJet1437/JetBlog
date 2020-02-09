FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev sqlite3 \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

RUN python sqlalchemy_db.py

RUN echo "sqlalchemy database created."

CMD ["python", "app.py"]
