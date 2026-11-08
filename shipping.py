
"""Shipping prices, delivery estimates, and free-shipping eligibility."""


def calculate_shipping(weight, destination="local", express=False,
                       member=False, insured=False):
    """Return the shipping price for a package."""
    if not isinstance(weight, (int, float)) or isinstance(weight, bool):
        raise TypeError("Weight must be a number")
    if weight <= 0:
        raise ValueError("Weight must be positive")
    if destination not in ("local", "national", "international"):
        raise ValueError("Invalid destination")

    if weight <= 2:
        cost = 5.0
    elif weight <= 10:
        cost = 10.0
    else:
        cost = 20.0

    if destination == "national":
        cost += 7.0
    elif destination == "international":
        cost += 20.0

    if express:
        cost += 8.0
    if insured:
        cost += 5.0
    if member:
        cost *= 0.90

    return round(cost, 2)


def estimate_delivery_days(destination="local", express=False):
    """Estimate delivery time based on destination and service."""
    if destination == "local":
        days = 2
    elif destination == "national":
        days = 5
    elif destination == "international":
        days = 10
    else:
        raise ValueError("Invalid destination")

    if express:
        days = max(1, days - 2)
    return days


def is_free_shipping_eligible(order_total, member=False):
    """Check whether an order qualifies for free shipping."""
    if order_total < 0:
        raise ValueError("Order total cannot be negative")
    if member:
        return order_total >= 50
    return order_total >= 75
