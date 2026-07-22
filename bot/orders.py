from bot.client import client
from binance.enums import *


def place_market_order(symbol, side, quantity):
    """Place a MARKET order."""
    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type=FUTURE_ORDER_TYPE_MARKET,
        quantity=quantity
    )


def place_limit_order(symbol, side, quantity, price):
    """Place a LIMIT order."""
    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type=FUTURE_ORDER_TYPE_LIMIT,
        quantity=quantity,
        price=price,
        timeInForce=TIME_IN_FORCE_GTC
    )