#!/usr/bin/env bash

source ~/.myrepo/bin/activate
python3 -m venv ~/.myrepo
make all

az webapp up --location westeurope -n flaskwebappproject
