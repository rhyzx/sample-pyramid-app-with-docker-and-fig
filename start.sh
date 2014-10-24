#!/usr/bin/env bash

# check db is ready
while ! ((>/dev/tcp/db/5432) &>/dev/null)
do
  echo "$(date) - waiting for db"
  sleep 1
done
echo "$(date) - db is ready, starting server"

python setup.py develop # setup egg_info (a bit of slow, add egg-info to git?)
initialize_app_db development.ini # init db
# TODO run FE assets build
pserve --reload development.ini # run server
