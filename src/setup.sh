#!/bin/sh

set -e

_HOME="$HOME/_manageur"

mv "$(dirname "$0")/_home/"* "$_HOME"

echo "source $_HOME/bashrc" >> "$HOME/.bashrc"

source "$HOME/.bashrc"

mv "$(dirname "$0")/gui" "$_HOME/gui"

cd "$_HOME/gui"

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python main.py