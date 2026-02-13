#!/bin/bash

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Activate virtual environment
source venv/bin/activate

# Start Streamlit in the background
streamlit run app.py --server.headless=true --server.port=8501 > /dev/null 2>&1 &
STREAMLIT_PID=$!

# Wait for Streamlit to start (adjust sleep time if needed)
sleep 2

# Launch Chromium in app mode
chromium --app=http://localhost:8501

# When Chromium closes, kill the Streamlit process
kill $STREAMLIT_PID
