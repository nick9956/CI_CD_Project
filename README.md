# Python Project Testing

This repository contains Python code that is tested using `unittest2` and `unittest-xml-reporting` for generating XML test reports. The project uses Poetry for dependency management.

## Prerequisites

- Python 3.12 or higher
- Poetry for managing Python packages and dependencies

## Setup

Before running the tests, you need to install the required dependencies. This project uses Poetry, so you can set up the environment and install all dependencies with the following commands:

```bash
# Install Poetry globally (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Navigate to the project directory
cd path/to/your/project

# Install dependencies using Poetry
poetry install
```

## Running Tests

To run the tests, execute the provided shell script `run_py_tests.sh`. This script handles test execution and ensures that the XML reports are generated in the appropriate directory. Use the following command:

```bash
./run_py_tests.sh
```

Make sure the script is executable. If it's not, you can make it executable by running:

```bash
chmod +x run_py_tests.sh
```

## Version 1.0.0 - Release Notes
- Added Jenkinsfile feature which allows to automate CI/CD process