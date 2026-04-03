# Binance Futures Trading Bot (Simplified USDT-M Testnet)

This is a Python-based trading bot designed to interact with the Binance Futures Testnet (USDT-M). It supports placing both MARKET and LIMIT orders for any USDT-M trading pair.

## Features
- **Language**: Python 3.x
- **CLI Framework**: Click with `Rich` for enhanced UX.
- **REST Layer**: `python-binance` library.
- **Support**: MARKET and LIMIT orders for BUY/SELL sides.
- **Logging**: Integrated logging to `logs/` directory and console.
- **Validation**: Strict input validation for symbols, quantities, and price.

## Prerequisites
- Python 3.8+
- Binance Testnet API Key and Secret. ([Get them here](https://testnet.binancefuture.com/))

## Setup Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/aps4934/trading_bot.git
    cd trading_bot
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**:
    Create a `.env` file from the example:
    ```bash
    cp .env.example .env
    ```
    Open `.env` and enter your Binance Testnet API credentials:
    ```env
    BINANCE_API_KEY=your_api_key_here
    BINANCE_API_SECRET=your_api_secret_here
    BINANCE_TESTNET=True
    ```

## Usage Examples

### Placing a MARKET Order
Buy 0.001 BTCUSDT at Market price:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Placing a LIMIT Order
Sell 0.01 ETHUSDT at 3500.50:
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.01 --price 3500.50
```

## Logs
All API requests, responses, and errors are logged under the `logs/` directory with a timestamped filename (e.g., `bot_20260403.log`).

## Project Structure
- `bot/`: Application logic package.
    - `client.py`: Wrapper around Binance API.
    - `orders.py`: High-level order management logic.
    - `validators.py`: CLI input validation logic.
    - `logging_config.py`: Centralized logging configuration.
- `cli.py`: The entry point for interacting with the bot.
- `requirements.txt`: Python package dependencies.
- `.env`: (Not committed) Private API keys.

## Assumptions
- The bot assumes the user has sufficient USDT margin in their Testnet account (USDT-M).
- Quantities and prices must meet Binance's minimum lot size and tick size requirements for each symbol.
- This version focuses on USDT-M Futures only.
