#!/usr/bin/env bash
set -euo pipefail

wget -q -O password.py.original https://github.com/ansible/ansible/raw/devel/lib/ansible/plugins/lookup/password.py
patch --input=password.patch --output=password.py password.py.original
