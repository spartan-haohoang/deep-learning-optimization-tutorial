#!/bin/bash

# Deep Learning Optimization Tutorial Setup Script
# This script sets up the environment for the deep learning optimization tutorial

set -e  # Exit on any error

echo "🚀 Setting up Deep Learning Optimization Tutorial Environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $PYTHON_VERSION detected. Python $REQUIRED_VERSION or higher is required."
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing core dependencies..."
pip install -r requirements.txt

# Install development dependencies if requested
if [ "$1" = "--dev" ]; then
    echo "🛠️  Installing development dependencies..."
    pip install -r requirements-dev.txt
fi

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p data scripts tests docs

# Validate data files
echo "🔍 Validating data files..."
python scripts/validate_data.py

echo "✅ Setup complete!"
echo ""
echo "To activate the environment in the future, run:"
echo "  source venv/bin/activate"
echo ""
echo "To start Jupyter Lab:"
echo "  jupyter lab"
echo ""
echo "To run tests:"
echo "  pytest"
