#!/usr/bin/env bash

set -e

sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install --upgrade capstone filebytes ropper

echo "Done. Use ropper -f <file> to test the tool."
