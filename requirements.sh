#!/bin/bash

# Upgrade pip
pip install --upgrade pip

# Install Python packages inside the virtual environment
pip install Pillow stepic cryptography pycryptodome colorama

echo -e "\nAll dependencies installed successfully in the virtual environment!"
