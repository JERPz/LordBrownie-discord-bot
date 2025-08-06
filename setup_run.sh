#!/bin/bash

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run the bot
python main.py
