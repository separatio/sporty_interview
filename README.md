# Introduction

This is a test framework using pytest and SeleniumBase.
The version of Python used is 3.10.

# Setup

All instructions below assume a working Python3 environment with pip installed. The project is currently using Python version 3.10.

1. Create the virtual environment by running `python -m venv venv`
2. Activate the virtual environment by running `source venv/bin/activate`
3. Install required packages by running `pip install -r requirements.txt`

# Running

Use the following command to run the test:

```bash
pytest tests/first_test.py --mobile --headed --demo --uc
```

# Docker

To use the dockerized version build and run the image:

```bash
docker build . -t sporty_interview
docker run -it sporty_interview
```

# Structure

- The support/pages folder contains the page objects
- The support folder contains the pages folder and the setUp/ tearDown code for the tests
- The tests folder contains the test required
- .github contains the CI Github Action
- there are pre-commit hooks running at every commit
- the drivers folder contains the chromedriver in case something goes wrong with what seleniumbase installs
