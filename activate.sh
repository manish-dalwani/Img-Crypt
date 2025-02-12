#!/bin/bash

sudo apt-get install -y python3-venv python3-pip

echo -e "\n🔄 Setting up Virtual Environment..."

# Remove existing env if exists
rm -rf env

# Create virtual environment if it doesn't exist
if [ ! -d "env" ]; then
    python3 -m venv env
fi

# Inform the user how to activate manually
echo -e "\nVirtual environment is set up!"

echo -e "\nRun 'source env/bin/activate' to activate virtual environment."
echo "Run 'deactivate' to deactivate the virtual environment."
