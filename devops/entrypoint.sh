#!/bin/bash
# https://docs.docker.com/config/containers/multi-service_container/
set -m

flask run &
#flask apscheduler &

rq worker -c rq_config &

fg %1