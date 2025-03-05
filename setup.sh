#!/bin/bash

# GitHub Repository Visibility Manager - Setup Script
# This script creates a virtual environment and installs required packages

# Exit on error
set -e

echo "GitHub Repository Visibility Manager - Setup"
echo "==========================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Create virtual environment
if [ -d "venv" ]; then
    echo "Virtual environment already exists."
else
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created successfully."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

echo ""
echo "Setup completed successfully!"
echo ""
echo "To use the GitHub Repository Visibility Manager:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run the script:"
echo "   python main.py"
echo ""
echo "3. When finished, deactivate the virtual environment:"
echo "   deactivate" 