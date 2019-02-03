FROM python:3.7.0-alpine3.8

MAINTAINER Javier Feliu <jfeliu@wanderin.dev>

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev

ENV INSTALL_PATH /fc
# ENV SECRET_KEY 'CmSAGpcN3dV85DByPqcCqHSY3Zh3'
# ENV DEBUG=False
# ENV TESTING=False
# ENV FLASK_CONFIG 'production'

RUN printenv

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN addgroup -S fc && adduser -S -g fc fc
USER fc

CMD gunicorn -b 0.0.0.0:5001 --access-logfile - --reload 'run:app'
