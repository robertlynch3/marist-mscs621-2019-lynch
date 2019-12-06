FROM python:3

LABEL MAINTANER Robert Lynch "robert.lynch3@marist.edu"

COPY . /

RUN pip install -r /requirements.txt

WORKDIR /app

CMD [ "python", "-u", "app.py" ]
