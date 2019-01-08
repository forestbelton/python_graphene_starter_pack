#!/bin/bash
set -euo pipefail

export FLASK_ENV=${FLASK_ENV:-development}
export FLASK_APP=app.py

# Navigate to project directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR/.."

flask run
