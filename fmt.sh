#!/bin/sh

autoflake --remove-all-unused-imports --remove-unused-variables -r -i .
isort --recursive --force-single-line .
black --line-length 79 .
flake8 --ignore=E741,E203,W503
