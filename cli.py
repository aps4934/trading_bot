import click
import logging
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint
from bot.logging_config import setup_logging
from bot.orders import handle_order
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price

# Set up logging for the session
logger = setup_logging()
console = Console()

@click.command()
@click.option('--symbol', required=True, callback=validate_symbol, help='Trading symbol (e.g., BTCUSDT)')
@click.option('--side', required=True, callback=validate_side, help='Order side (BUY/SELL)')
@click.option('--type', 'order_type', required=True, callback=validate_order_type, help='Order type (MARKET/LIMIT)')
@click.option('--quantity', required=True, callback=validate_quantity, help='Trade quantity')
@click.option('--price', callback=validate_price, default=None, help='Price (required for LIMIT orders)')
def main(symbol, side, order_type, quantity, price):
    """
    Binance Futures Trading Bot (Testnet USDT-M)
    Place MARKET or LIMIT orders on the futures testnet.
    """
    # UI: Print order request summary
    rprint(Panel.fit(
        f"[bold cyan]Order Request Summary[/bold cyan]\n"
        f"Symbol: [yellow]{symbol}[/yellow]\n"
        f"Side:   [magenta]{side}[/magenta]\n"
        f"Type:   [green]{order_type}[/green]\n"
        f"Qty:    [white]{quantity}[/white]\n"
        f"Price:  [white]{price if price is not None else 'N/A'}[/white]",
        title="Trading Bot Request", border_style="blue"
    ))

    # Extra validation for LIMIT price
    if order_type.upper() == 'LIMIT' and price is None:
        console.print("[bold red]Error:[/bold red] Price is required for LIMIT orders.")
        return

    try:
        # Place the order through the handler
        response = handle_order(symbol, side, order_type, quantity, price)

        # Print success UI
        if response:
            console.print("[bold green]✔ Success: Order placed on Testnet.[/bold green]\n")

            # Create an order details table
            table = Table(title="Order Response Details", show_header=True, header_style="bold blue")
            table.add_column("Field", style="dim", width=15)
            table.add_column("Value", style="cyan")

            table.add_row("OrderID", str(response.get('orderId')))
            table.add_row("Status", str(response.get('status')))
            table.add_row("Symbol", str(response.get('symbol')))
            table.add_row("Executed Qty", str(response.get('executedQty')))
            table.add_row("Avg Price", str(response.get('avgPrice', 'N/A')))
            table.add_row("Side", str(response.get('side')))
            table.add_row("Type", str(response.get('type')))

            console.print(table)
            logger.info(f"Successfully processed {order_type} {side} for {symbol}. OrderID: {response.get('orderId')}")
        else:
            console.print("[bold red]× Error: Order returned no response.[/bold red]")

    except Exception as e:
        console.print(f"[bold red]× API / Order Error:[/bold red] {str(e)}")
        logger.error(f"Order failed for {symbol}: {str(e)}")

if __name__ == '__main__':
    main()
