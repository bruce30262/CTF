#!/usr/bin/env bash

set -e

if command -v nala && command -v uv && [ -e $HOME/.venv/bin/activate ]
then
    # have nala, uv and default .venv, can use fast install
    source $HOME/.venv/bin/activate
    uv pip install --upgrade capstone filebytes ropper
else
    # default install method
    sudo python3 -m pip install --upgrade pip
    sudo python3 -m pip install --upgrade capstone filebytes ropper 
fi

echo "Done. Use ropper -f <file> to test the tool."
