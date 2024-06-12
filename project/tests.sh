#!/bin/bash
file_dir="$(dirname "$0")"

pytest "$file_dir/tests/test_pipeline.py"
