"""Set of functions for Queueing Theory Course."""

import sys
from math import factorial, exp


def input_parameters():
    """Return input parameters of valid type."""
    values_number = int(input('Input n (default: 10): ') or 10)
    _lambda = float(input('Input lambda (default: 0.5): ') or 0.5)
    time = int(input('Input t (default: 1): ') or 1)

    return values_number, _lambda, time


def distribute_poisson():
    """Return tuple of `n` values distributed using Poisson method.

    Task 1 and 2 from course credit.
    """
    values_number, _lambda, time = input_parameters()
    # Factorial argument cannot be negative
    while _lambda * time <= 0.0 and time < 0:
        print('lambda * time should be positive.\n Please input correct values\n')
        values_number, _lambda, time = input_parameters()

    return tuple(
        ((_lambda * time) ** k) * exp(-_lambda * time) / factorial(k)
        for k in range(values_number)
    )


def distribute_exponentially():
    """Return tuple of `n` values distributed using Exponential method.

    Task 3 from course credit.
    """
    values_number = int(input('Input n (default: 10): ') or 10)
    _lambda = float(input('Input lambda (default: 0.5): ') or 0.5)

    return tuple(
        (1 - exp(-_lambda * x)) if x > 0 else 0
        for x in range(values_number)
    )


if __name__ == '__main__':
    DISTRIBUTION = sys.argv[1]

    if DISTRIBUTION == 'exp':
        print(f'Results: {distribute_exponentially()}')
    elif DISTRIBUTION == 'poisson':
        print(f'Results: {distribute_poisson()}')
    else:
        print('Please specify distribution method: exponential or poisson')
