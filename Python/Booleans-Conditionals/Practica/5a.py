def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion


def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return  ketchup and mustard and onion

# Check your answer

q5.a.check()
