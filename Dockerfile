FROM python:3.8
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install netcat -y
# RUN python manage.py migrate --noinput

COPY . /app
RUN mkdir /app/static

# COPY ./entrypoint.sh /app
# RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"]
