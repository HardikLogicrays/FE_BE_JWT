FROM python:3-alpine

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

RUN ls && pwd

LABEL author="HARDIK.S"

EXPOSE 8000

RUN python manage.py makemigrations app

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
