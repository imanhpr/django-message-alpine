FROM python:alpine3.16
RUN pip install Django==4.0.6
RUN mkdir /myapp
COPY . /myapp
WORKDIR /myapp
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000