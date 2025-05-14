# This project is used to do tasks using browser automation

## NOTE

- Use python 3.11 or higher

## Create a virtual environment

```bash
python3 -m venv agent-env
```

## Activate the virtual environment

```bash

source agent-env/bin/activate
```

## install chromium

```bash
brew install --cask chromium

```

## Create a .env file

```bash
touch .env
```

## NOTE

- Add API Key of OpenAI in the .env file

```bash

OPENAI_API_KEY=your_openai_api_key
```

## Install the requirements

```bash
pip install -r requirements.txt
```

## Run the code

```bash
python main.py
```