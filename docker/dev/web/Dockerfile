# pull official base image
FROM python:3.10.0-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	TZ=Europe/Moscow \
	LANG=C.UTF-8 \
	APP_HOME=/usr/src/web

WORKDIR $APP_HOME

ARG GID=1000
ARG UID=1000
ARG USER=ubuntu

# install dependencies
RUN apk update \
    && apk add --no-cache curl postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev build-base \
    # install Pillow dependencies
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev \
	  && pip install --upgrade pip \
    && addgroup -g $GID -S $USER \
	  && adduser -S $USER -G $USER --disabled-password --uid "$UID"


COPY ./web/src/requirements  ./requirements
RUN pip install -r ./requirements/requirements.txt

COPY --chown=$USER:$USER ./docker/dev/web/entrypoints /
COPY --chown=$USER:$USER ./web $APP_HOME

RUN chmod +x /*.sh \
    && mkdir -p $APP_HOME/static \
    && chown -R $USER:$USER $APP_HOME/static \
    && flake8 .
ENTRYPOINT ["/entrypoint.sh"]

USER $USER
