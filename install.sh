#!/bin/bash

set -e

echo "======================================"
echo "Installing Img-Crypt..."
echo "======================================"

# Install required packages
if ! sudo apt update; then
    echo "Warning: apt update failed."
    echo "Continuing installation..."
fi
sudo apt install -y python3 python3-pip dos2unix

# Convert Windows line endings (if any)
dos2unix img-crypt.py 2>/dev/null || true

# Make executable
chmod +x img-crypt.py

# Install Python dependencies
python3 -m pip install --break-system-packages -r requirements.txt

# Install globally
sudo install -m755 img-crypt.py /usr/local/bin/img-crypt

echo ""
echo "======================================"
echo "Installation Completed Successfully!"
echo ""
echo "Run using:"
echo ""
echo "img-crypt"
echo "======================================"
