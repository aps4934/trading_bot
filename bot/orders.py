import logging
from bot.client import BinanceFuturesClient

logger = logging.getLogger("trading_bot.orders")

def handle_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Business logic for handling different order types."""
    try:
        # Side/OrderType should already be validated (from CLI or elsewhere)
        # Assuming you've already handled .env keys via direct instantiation or client's internal load_dotenv
        client = BinanceFuturesClient()

        logger.info(f"Preparing {order_type} {side} order for {quantity} {symbol}")

        if order_type.upper() == 'MARKET':
            response = client.place_market_order(symbol.upper(), side.upper(), quantity)
        elif order_type.upper() == 'LIMIT':
            if price is None:
                raise ValueError("Price is required for LIMIT order.")
            response = client.place_limit_order(symbol.upper(), side.upper(), quantity, price)
        else:
            raise ValueError(f"Unsupported order type: {order_type}")

        # Summary of request after client was successful
        logger.info(f"Order {order_type} {side} {quantity} {symbol} successfully sent.")
        return response

    except Exception as e:
        logger.error(f"Order failed during processing: {str(e)}")
        # return None or raise
        raise
