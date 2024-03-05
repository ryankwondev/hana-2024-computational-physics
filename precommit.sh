#!/usr/bin/env bash

black .
pip freeze > requirements.txt
