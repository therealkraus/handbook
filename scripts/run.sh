#!/bin/bash

# Get the parent directory of the current script and change the current directory to it
SCRIPT_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PARENT_DIR"

if [ ! -f "venv/bin/activate" ]; then
    python3.12 -m venv venv
fi

source venv/bin/activate

python3.12 -m pip install --upgrade pip

pip install -r requirements.txt

cd "$PARENT_DIR/handbook"

mkdocs build

gunicorn --workers 4 --bind 0.0.0.0:8000 wsgi:app

