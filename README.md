# Algorithmic trading Final Project: XAUUSD EMA crossover + RSI confirmation strategy

## Group members

- [J56164](https://github.com/J56164)
- [Siamrat27](https://github.com/Siamrat27)
- [NattawitMana](https://github.com/NattawitMana)

## Overview

- XAUUSD EMA crossover + RSI confirmation strategy
- The main code and explanation is in the `notebooks/xauusd_backtesting.ipynb` notebook

## Installation

- Install [uv](https://docs.astral.sh/uv/#installation)
- Environment setup: Run `uv sync` to create/sync uv environment
- Database setup (optional, in case you want to try EzyQuant Thai stock data): Download EzyQuant-compatible database into `data/ezyquant.db`
- Running notebooks:
  - Download [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) Visual Studio Code extension
  - In Visual Studio Code, Ctrl+P > "Python: Select Interpreter" > Select your environment's interpreter path
  - Open a notebook and you can now run code blocks

## Tech Stack

- Python 3.12+
- uv (package manager)
- vectorbt, backtesting.py (backtesting frameworks)
  - Primarily uses backtesting.py
- tvDatafeed, ezyquant (data sources)
  - Primarily uses tvDatafeed

## Directory Structure

```text
- src/              # Core Python module
- notebooks/        # Jupyter notebooks (backtesting)
- data/             # Data directory
```
