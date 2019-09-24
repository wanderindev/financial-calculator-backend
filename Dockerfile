FROM alpine

MAINTAINER Javier Feliu <javier@wanderin.dev>

COPY requirements.txt /tmp/requirements.txt

RUN apk add --no-cache \
    python3 \
    bash \
    nginx \
    uwsgi \
    uwsgi-python3 \
    supervisor && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY nginx.conf /etc/nginx/
COPY fc-nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/supervisord.conf

ENV INSTALL_PATH /app
ENV FLASK_CONFIG production
ENV SECRET_KEY mysecretkey
ENV DEBUG=False
ENV TESTING=False

EXPOSE 80

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY app.py .
COPY config.py .
COPY run.py .
COPY /calculators ./calculators

CMD ["/usr/bin/supervisord"]
