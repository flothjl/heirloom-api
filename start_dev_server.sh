#!/bin/bash
source ./env/bin/activate
export FLASK_APP=heirloom_api
export FLASK_ENV=development
flask run
