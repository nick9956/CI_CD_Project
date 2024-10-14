#!/bin/bash

# Navigate to the test directory
cd tests

# Run the tests using the Python unittest module
poetry run python string_test.py

# Return to the root directory
cd ..