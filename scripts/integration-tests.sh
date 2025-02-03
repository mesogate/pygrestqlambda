#!/bin/bash
set -euo pipefail

# Install development dependencies with pip
pip install .[dev]

echo "Running pytest for integration tests"
pytest \
  -o log_cli=true \
  --log-cli-level=INFO \
  tests/integration
