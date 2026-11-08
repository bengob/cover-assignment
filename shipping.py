
def calculate_shipping(weight, express=False, member=False):
    if weight <= 0:
        raise ValueError("Weight must be positive")

    if weight <= 2:
        cost = 5
    else:
        cost = 10

    if express:
        cost += 8

    if member:
        cost *= 0.9

    return cost
