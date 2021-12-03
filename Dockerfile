FROM python:3.9

RUN pip install django

COPY . /app
WORKDIR /app

RUN ls -la

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
