#!/bin/bash

export FLASK_APP=flasknx
export FLASK_ENV=development
export DEBUG_METRICS=True

flask run 5000
