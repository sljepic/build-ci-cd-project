#!/usr/bin/env bash

cd build-ci-cd-project
az webapp up --sku F1 -n flask_webapp_project_2
az webapp config set -g build-ci-cd-project -n flask_webapp_project_2
