#!/bin/bash

# kill before start
pgrep gunicorn | xargs kill -s 9
# start
nohup gunicorn -k gevent -w 5 -b 0.0.0.0:5000 api:app &