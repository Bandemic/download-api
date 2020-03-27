# BanDemic Public API

Public API for fetching anonymous identifiers of SARS-CoV-2 positive users

## Requirements

- Python 3.8+
- MongoDB database

## Installation

Install and initialize [Poetry](https://python-poetry.org/docs). Run

```bash
poetry install
```

## Configuration

Copy the `config.py.example` to `config.py` and adjust the database connection URI.

## Development

Run the local Flask development server using

```bash
export POETRY_ENV="development"
poetry run flask run
```
