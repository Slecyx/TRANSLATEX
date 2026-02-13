#!/bin/bash
# TranslateX Quick Setup Script
# Automated installation for Linux/macOS

set -e

echo "🌌 TranslateX Prime - Installation Wizard"
echo "==========================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION detected"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check for LibreOffice (optional but recommended)
if command -v libreoffice &> /dev/null; then
    echo "✅ LibreOffice detected (PDF conversion enabled)"
else
    echo "⚠️  LibreOffice not found. Install it for optimal PDF/PPTX conversion:"
    echo "   Ubuntu/Debian: sudo apt install libreoffice"
    echo "   Fedora: sudo dnf install libreoffice"
    echo "   macOS: brew install --cask libreoffice"
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "🚀 To start TranslateX, run:"
echo "   ./run.sh"
echo ""
echo "Or manually:"
echo "   source venv/bin/activate"
echo "   streamlit run app.py"
echo ""
