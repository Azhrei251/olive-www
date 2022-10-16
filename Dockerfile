FROM python:3
COPY . /django-site
WORKDIR /django-site
RUN pip install -r requirements.txt
RUN python web/manage.py collectstatic –noinput
CMD python web/server.py
