#!/bin/bash

cd ~/app
pip3 install -r requirements.txt
nohup uvicorn app.main:app --host 0.0.0.0 --port 80 > output.log 2>&1 &
