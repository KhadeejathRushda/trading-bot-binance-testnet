import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import logger


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        if args.price:
            print(f"Price    : {args.price}")

        logger.info(f"Order Request: {vars(args)}")

        if args.type.upper() == "MARKET":
            response = place_market_order(
                args.symbol,
                args.side.upper(),
                args.quantity
            )
        else:
            response = place_limit_order(
                args.symbol,
                args.side.upper(),
                args.quantity,
                args.price
            )

        print("\n✅ Order Placed Successfully!")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        avg_price = response.get("avgPrice") or "N/A"
        print(f"Average Price : {avg_price}")
        logger.info(f"Order Response: {response}")

    except Exception as e:
        logger.error(str(e))
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()