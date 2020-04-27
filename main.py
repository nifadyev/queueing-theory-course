"""Set of functions for Queueing Theory Course."""

import sys
from random import random
from math import factorial, exp


def input_parameters():
    """Return input parameters of valid type."""
    _lambda = float(input('Input lambda (default: 0.5): ') or 0.5)
    time = int(input('Input t (default: 1): ') or 1)

    return _lambda, time


def distribute_poisson(_lambda, time, k):
    """Return tuple of `n` values distributed using Poisson method."""
    return ((_lambda * time) ** k) * exp(-_lambda * time) / factorial(k)


def generate_value_poisson():
    _lambda, time = input_parameters()
    # Factorial argument cannot be negative
    while _lambda * time <= 0.0 and time < 0:
        print('lambda * time should be positive.\n Please input correct values\n')
        _lambda, time = input_parameters()

    for _ in range(10):
        random_value = random()
        result = 0

        probabilites_sum = distribute_poisson(_lambda, time, result)
        while random_value > probabilites_sum:
            result += 1
            probabilites_sum += distribute_poisson(_lambda, time, result)

        yield result


def distribute_exponentially():
    """Return tuple of `n` values distributed using Exponential method."""
    values_number = int(input('Input n (default: 10): ') or 10)
    _lambda = float(input('Input lambda (default: 0.5): ') or 0.5)

    for _ in range(values_number):
        x = random()
        yield (1 - exp(-_lambda * x)) if x > 0 else 0


if __name__ == '__main__':
    DISTRIBUTION = sys.argv[1]

    if DISTRIBUTION == 'exp':
        print(f'Results: {tuple(distribute_exponentially())}')
    elif DISTRIBUTION == 'poisson':
        print(f'Results: {tuple(generate_value_poisson())}')
    else:
        print('Please specify distribution method: exponential or poisson')
