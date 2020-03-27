# BanDemic Public API

Public API for fetching anonymous identifiers of SARS-CoV-2 positive users

## Requirements

- Python 3.8+
- MongoDB database

<details>
  <summary>Quick start Python 3.8 (Debian based Linux)</summary>
  
  ```bash
sudo apt install python3.8 python3.8-pip
sudo update-alternatives --config python3
  ```
  Then select the correct Python version.
</details>

## Installation

Install and initialize [Poetry](https://python-poetry.org/docs). Run

```bash
poetry install
```
<details>
  <summary>Quick start Poetry (UNIX)</summary>
  
  ```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
source ~/.poetry/env
  ```
  
</details>

## Configuration

Copy the `config.py.example` to `config.py` and adjust the database connection URI.

## Development

Run the local Flask development server using

```bash
export POETRY_ENV="development"
poetry run flask run
```
Then browse to http://localhost:5000/v1/cases?uuid=af7af6b6-eb02-4d12-b554-f5cb089afc5d for example.
