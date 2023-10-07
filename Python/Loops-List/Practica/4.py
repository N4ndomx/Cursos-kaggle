def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    # Play slot machine n_runs times, calculate payout of each
    pagos = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    beneficio = sum(pagos) / n_runs
    return beneficio
    pass

estimate_average_slot_payout(10000000)