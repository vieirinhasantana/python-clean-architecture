FROM python:rc-alpine

RUN apk update && apk upgrade

ENV TZ=America/Sao_Paulo

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements/requirements.txt

ENTRYPOINT ["python", "app.py"]
