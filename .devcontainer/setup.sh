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
./.venv/bin/pip install --no-cache-dir -r ${containerWorkspaceFolder}/requirements.txt

# 3. Register the Virtual Environment as a Jupyter Kernel
echo "Registering .venv as a Jupyter Kernel ('OpenBB Exp')..."
./.venv/bin/python -m ipykernel install --name=magentic_algo_venv --display-name 'OpenBB Exp'

# --- NEW STEP: Claude Code Installation ---
# 4. Install Claude Code CLI
echo "Installing Anthropic Claude Code CLI via npm..."
# The -g flag installs the package globally so 'claude' command is available in the shell.
# NOTE: Ensure your Dockerfile has Node.js/npm installed.
sudo npm install -g @anthropic-ai/claude-code
# --- END NEW STEP ---

echo "--- Setup complete! ---"