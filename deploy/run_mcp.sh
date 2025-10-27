#!/bin/bash

# --- Configuration ---
# Set the path to your virtual environment relative to the script's execution location
VENV_PATH="../.venv"

# The command to execute
COMMAND="openbb-mcp"

# --- Script Execution ---

# Check if the virtual environment directory exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Error: Virtual environment not found at $VENV_PATH" >&2
    echo "Please run your devcontainer's postCreateCommand or 'python3 -m venv .venv' first." >&2
    exit 1
fi

# 1. Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_PATH/bin/activate"

# Check if activation was successful (e.g., if the 'openbb-mcp' command is now in PATH)
if command -v "$COMMAND" >/dev/null 2>&1; then
    echo "Virtual environment activated successfully."
    
    # 2. Execute the command
    echo "Starting $COMMAND..."
    # The 'exec' command replaces the current shell with the openbb-mcp process.
    # This is a clean way to run the final command in a script.
    exec "$COMMAND"
else
    echo "Error: Could not find '$COMMAND' after activating virtual environment." >&2
    echo "Please ensure the OpenBB-MCP package is installed: 'pip install openbb-mcp'" >&2
    deactivate # Deactivate before exiting
    exit 1
