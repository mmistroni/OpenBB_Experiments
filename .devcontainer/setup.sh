#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- Starting postCreate setup script ---"

# 1. Create a Python Virtual Environment
echo "Creating Python virtual environment (.venv)..."
python3 -m venv .venv

# 2. Activate and Install Dependencies
# Use the full path to the executable to ensure the correct venv is used.
echo "Installing dependencies from requirements.txt..."
./.venv/bin/pip install --no-cache-dir -r requirements.txt

# 3. Register the Virtual Environment as a Jupyter Kernel
echo "Registering .venv as a Jupyter Kernel ('OpenBB Exp')..."
./.venv/bin/python -m ipykernel install --name=magentic_algo_venv --display-name 'OpenBB Exp'

echo "--- Setup complete! ---"