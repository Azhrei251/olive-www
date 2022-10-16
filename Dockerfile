FROM python:3
COPY . /django-site
WORKDIR /django-site
RUN pip install -r requirements.txt
RUN mkdir /logs
CMD python web/server.py
