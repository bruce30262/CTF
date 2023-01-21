#!/usr/bin/env bash
set -e

sudo apt update
sudo apt install -y python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install --upgrade pwntools

echo "Done."
