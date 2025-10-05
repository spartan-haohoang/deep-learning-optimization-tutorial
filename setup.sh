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

# Install UV if not present
if ! command -v uv &> /dev/null; then
    echo "📦 Installing UV package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

echo "✅ UV package manager ready"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies using UV
echo "📚 Installing dependencies with UV..."
uv sync --dev

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p data scripts tests docs models logs

# Validate data files
echo "🔍 Validating data files..."
uv run python scripts/validate_data.py

# Run initial tests
echo "🧪 Running initial tests..."
uv run pytest --tb=short

echo "✅ Setup complete!"
echo ""
echo "To activate the environment in the future, run:"
echo "  source venv/bin/activate"
echo ""
echo "To start Jupyter Lab:"
echo "  uv run jupyter lab"
echo ""
echo "To run tests:"
echo "  uv run pytest"
echo ""
echo "To start with Docker:"
echo "  docker-compose up"
