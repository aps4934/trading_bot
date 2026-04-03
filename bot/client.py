import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv

logger = logging.getLogger("trading_bot.client")

class BinanceFuturesClient:
    def __init__(self, api_key: str = None, api_secret: str = None, testnet: bool = True):
        # Allow loading from system environment and/or .env if not provided.
        load_dotenv()
        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET")
        self.testnet = testnet

        if not self.api_key or not self.api_secret:
            logger.error("Missing Binance API Key or Secret.")
            raise ValueError("Missing Binance API Key or Secret. Ensure they are in your .env or system environment.")

        # Initialize the client. python-binance handles signatures and testnet vs prod endpoints.
        # NOTE: For futures, we typically use the futures client methods.
        self.client = Client(self.api_key, self.api_secret, testnet=self.testnet)

        # Confirm the client can connect.
        try:
            # Check server time to verify connectivity
            server_time = self.client.get_server_time()
            logger.info("Connected to Binance API. Server Time: %s", server_time['serverTime'])
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.error(f"Failed to connect to Binance API: {str(e)}")
            raise

    def place_market_order(self, symbol: str, side: str, quantity: float):
        """Places a MARKET order on USDT-M Futures."""
        try:
            logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"Market order response: {order}")
            return order
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.error(f"Error placing MARKET order: {str(e)}")
            raise

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        """Places a LIMIT order on USDT-M Futures."""
        try:
            # GTC = Good 'Til Cancelled (Standard for limit orders)
            logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} at {price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=str(price)  # price must be string or float. string is safer for precision.
            )
            logger.info(f"Limit order response: {order}")
            return order
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.error(f"Error placing LIMIT order: {str(e)}")
            raise
