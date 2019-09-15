# flasknx

Just a example app with flask + uwsgi + nginx

## Tested

- Python 3.7.3
- Flask 1.1.1
- uWSGI 2.0.18
- Nginx 1.15.8

## How

```bash
python -m venv venv
. venv/bin/active

pip install -e .

bash bin/start.sh
```

## With docker

```bash
docker build -t flasknx:0.0.1 .
docker run --rm -P --name flasknx flasknx:0.0.1
docker inspect --format '{{ .NetworkSettings.Ports }}' flasknx

port=$(docker inspect --format '{{ .NetworkSettings.Ports }}' flasknx | awk '{print $4}' | tr -dc '0-9')

curl "0.0.0.0:${port}/healthcheck"
```

## Info

Image size: 993MB (so bad)  
Memory used: ~50Mb
