# Trading Bot Implementation Walkthrough

This document outlines the architecture and execution of the simplified Binance Futures Trading Bot.

## Project Structure
The project follows a modular design for scalability and maintainability:

```text
trading_bot/
├── bot/                # Core logic package
│   ├── client.py        # API abstraction layer
│   ├── orders.py        # Business logic for orders
│   ├── validators.py    # Input validation rules
│   └── logging_config.py# Centralized logging setup
├── logs/               # Log output directory
├── cli.py              # CLI entry point
├── README.md           # Documentation
└── requirements.txt    # Component dependencies
```

## Core Modules

### 1. Client Layer (`bot/client.py`)
- Uses `python-binance` to manage connections.
- Configured specifically for the **Binance Futures Testnet**.
- Implements `place_market_order` and `place_limit_order`.
- Error handling catches `BinanceAPIException` to provide meaningful feedback.

### 2. Business Logic (`bot/orders.py`)
- Acts as a mediator between the CLI and the API client.
- Orchestrates order placement by mapping the CLI request to the appropriate client call.
- Summarizes requests before and after execution.

### 3. CLI Layer (`cli.py`)
- Built with `click` for command parsing and `rich` for aesthetic terminal output.
- Features real-time field validation for quantities and symbols.
- Displays order response data in a clean, formatted table.

### 4. Logging (`bot/logging_config.py`)
- Configures two handlers:
    - **Console**: Uses `rich` for colored, readable logs during development.
    - **File**: Outputs to `logs/bot_YYYYMMDD.log` for debugging and auditing.

## How to Test
1.  Install dependencies: `pip install -r requirements.txt`.
2.  Add your API Key and Secret to a `.env` file (see `.env.example`).
3.  Execute an order:
    ```bash
    python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005
    ```

## Final Deliverables
- Fully functional source code.
- README with setup and examples.
- Sample logs showing both MARKET and LIMIT order outputs.
- Pushed to the provided GitHub repository: [aps4934/trading_bot](https://github.com/aps4934/trading_bot).
