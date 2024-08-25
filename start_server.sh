#!/bin/bash

python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the dependencies
pip install "fastapi[standard]"

# Start the server
fastapi dev main.py