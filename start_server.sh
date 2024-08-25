#!/bin/bash

python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the dependencies
pip install "fastapi[standard]"
pip install -r requirements.txt

# Start the server
fastapi dev main.py