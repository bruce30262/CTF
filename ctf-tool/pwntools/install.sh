#!/usr/bin/env bash
set -e

if command -v nala && command -v uv && [ -e $HOME/.venv/bin/activate ]
then
    # have nala, uv and default .venv, can use fast install
    sudo nala update
    sudo nala install -y python3 python3-dev git libssl-dev libffi-dev build-essential
    source $HOME/.venv/bin/activate
    uv pip install --upgrade pwntools
else
    # default install method
    sudo apt update
    sudo apt install -y python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
    sudo python3 -m pip install --upgrade pip
    sudo python3 -m pip install --upgrade pwntools
fi

echo "Done."
