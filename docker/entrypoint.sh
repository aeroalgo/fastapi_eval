#!/usr/bin/env sh

set -e
gunicorn main:app --bind 0.0.0.0:8003 -w 4 -k uvicorn.workers.UvicornWorker