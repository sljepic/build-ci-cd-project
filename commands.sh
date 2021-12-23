#!/usr/bin/env bash

source ~/.myrepo/bin/activate
python3 -m venv ~/.myrepo
make all

az webapp up --sku F1 -n flaskwebappproject2
