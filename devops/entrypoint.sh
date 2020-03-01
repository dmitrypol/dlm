#!/bin/bash
# https://docs.docker.com/config/containers/multi-service_container/
set -m

flask run -h 0.0.0.0 -p 5000

# gunicorn app:APP --bind 0.0.0.0:5000 --workers 2 --threads 2 --reload --pid tmp/gunicorn.pid

fg %1