FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV UWSGI_INI /app/flasknx/uwsgi.ini

COPY . /app

WORKDIR /app

RUN pip install -e .

EXPOSE 80
