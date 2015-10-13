FROM python:2.7

RUN mkdir /srv/app

WORKDIR /srv/app

COPY app.py /srv/app/app.py
COPY requirements.txt /srv/app/requirements.txt

RUN pip install -r /srv/app/requirements.txt

EXPOSE 8000
CMD python /srv/app/app.py
