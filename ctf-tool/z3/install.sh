#!/usr/bin/env bash

set -e

if command -v nala && command -v uv && [ -e $HOME/.venv/bin/activate ]
then
    # have nala, uv and default .venv, can use fast install
    source $HOME/.venv/bin/activate
    uv pip install --upgrade z3-solver
else
    # default install method
    sudo python3 -m pip install --upgrade pip
    sudo python3 -m pip install --upgrade z3-solver
fi

echo "Done. Run z3_test.py to test z3 ( It should print out \"NOHACK4UXWRATHOFKFUHRERX\")"

