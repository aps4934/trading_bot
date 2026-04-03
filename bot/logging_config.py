import logging
import os
from datetime import datetime
from rich.logging import RichHandler

def setup_logging():
    # Create logs directory if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Log file name with timestamp
    log_file = os.path.join(log_dir, f"bot_{datetime.now().strftime('%Y%m%d')}.log")

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            RichHandler(rich_tracebacks=True),
            logging.FileHandler(log_file)
        ]
    )

    return logging.getLogger("trading_bot")
