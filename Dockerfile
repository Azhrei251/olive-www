FROM python:3
COPY . /ShoppingListServer
WORKDIR /ShoppingListServer
RUN pip install -r requirements.txt
RUN mkdir /logs
CMD python listsite/server.py
