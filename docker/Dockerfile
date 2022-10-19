FROM python:3.8.1-slim-buster

COPY --chown=www-data:www-data fastapi_eval/app/backend/build/requirements.txt var/app/backend/build/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r var/app/backend/build/requirements.txt

VOLUME /var
EXPOSE 8003
WORKDIR /var/app/backend/src
COPY --chown=www-data:www-data fastapi_eval/docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]