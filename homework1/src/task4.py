"""Task 4: Functions and Duck Typing."""


def calculate_discount(price, discount):
    """
    Calculate the final price after applying a discount percentage.

    Thanks to duck typing, 'price' and 'discount' can be any numeric type
    (int, float, Decimal, etc.) as long as they support arithmetic operators.

    Args:
        price:    Original price of the product (any numeric type).
        discount: Discount percentage to apply, e.g. 20 means 20% off.

    Returns:
        The final price after the discount, as a float.

    Raises:
        TypeError:  If price or discount do not support required arithmetic.
        ValueError: If price is negative or discount is not in [0, 100].
    """
    # Input validation
    try:
        price + 0
        discount + 0
    except TypeError:
        raise TypeError("price and discount must be numeric types.")

    if price < 0:
        raise ValueError("price must be non-negative.")
    if not (0 <= discount <= 100):
        raise ValueError("discount must be between 0 and 100.")

    final_price = price * (1 - discount / 100)
    return float(final_price)


if __name__ == "__main__":
    print(calculate_discount(100, 20))       # int  -> 80.0
    print(calculate_discount(49.99, 10.5))   # float -> 44.740...
    print(calculate_discount(200, 0))        # no discount
    print(calculate_discount(200, 100))      # 100% off -> 0.0
