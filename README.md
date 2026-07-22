# Binance Futures Testnet Trading Bot

## Overview

This project is a simple Python-based trading bot that connects to the Binance Futures Testnet. It allows users to place BUY and SELL Market or Limit orders through a Command Line Interface (CLI). The application includes input validation, logging, and error handling.

## Features

- Place Market Orders
- Place Limit Orders
- Supports BUY and SELL
- Command Line Interface (CLI)
- Input Validation
- API Request and Response Logging
- Exception Handling

## Project Structure

```
trading_bot/
│── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
│── logs/
│   └── trading.log
│
│── cli.py
│── test_connection.py
│── requirements.txt
│── .env
│── README.md
```

## Requirements

- Python 3.x
- Binance Futures Testnet Account
- API Key and Secret

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/trading-bot-binance-testnet.git
cd trading-bot-binance-testnet
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

## Logging

All API requests, responses, and errors are stored in:

```
logs/trading.log
```

## Assumptions

- The application uses Binance Futures Testnet (Demo Trading).
- API credentials are stored in a `.env` file.
- Only MARKET and LIMIT orders are implemented.

## Author

Khadeejath Rushda
