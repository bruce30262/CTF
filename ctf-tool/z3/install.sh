#!/usr/bin/env bash

set -e

sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install --upgrade z3-solver

echo "Done. Run z3_test.py to test z3 ( It should print out \"NOHACK4UXWRATHOFKFUHRERX\")"

