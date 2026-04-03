import click

def validate_symbol(ctx, param, value):
    if not value or len(value) < 3:
        raise click.BadParameter("Symbol must be at least 3 characters (e.g. BTCUSDT)")
    return value.upper()

def validate_side(ctx, param, value):
    if value.upper() not in ['BUY', 'SELL']:
        raise click.BadParameter("Side must be either 'BUY' or 'SELL'")
    return value.upper()

def validate_order_type(ctx, param, value):
    if value.upper() not in ['MARKET', 'LIMIT']:
        raise click.BadParameter("Order type must be either 'MARKET' or 'LIMIT'")
    return value.upper()

def validate_quantity(ctx, param, value):
    try:
        q = float(value)
        if q <= 0:
            raise click.BadParameter("Quantity must be greater than 0")
        return q
    except ValueError:
        raise click.BadParameter("Quantity must be a number")

def validate_price(ctx, param, value):
    # Price is only required for LIMIT orders.
    # In click, this is handled via logic in the command if requested.
    if value is None:
        return None
    try:
        p = float(value)
        if p <= 0:
            raise click.BadParameter("Price must be greater than 0")
        return p
    except ValueError:
        raise click.BadParameter("Price must be a number")
