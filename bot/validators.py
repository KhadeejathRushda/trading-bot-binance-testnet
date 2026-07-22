def validate_order(symbol, side, order_type, quantity, price=None):
    # Check symbol
    if not symbol:
        raise ValueError("Symbol is required.")

    # Check side
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    # Check order type
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    # Check quantity
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    # Check price for LIMIT orders
    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Price is required for LIMIT orders.")