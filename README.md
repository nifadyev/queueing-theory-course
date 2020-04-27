# Queueing Theory Course

Tasks for getting credit.

## Task 1

Poisson distribution with parameters n, lambda and t:

```Python
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
```

## Task 2

Random 10 values with lambda = 0.5:

```bash
$ python main.py poisson
Input lambda (default: 0.5): 0.5
Input t (default: 1): 1

Results: (1, 0, 2, 1, 1, 0, 2, 0, 1, 1)
```


## Task 3

Exponential distribution with parameters n and lambda:

```Python
def distribute_exponentially():
    """Return tuple of `n` values distributed using Exponential method."""
    values_number = int(input('Input n (default: 10): ') or 10)
    _lambda = float(input('Input lambda (default: 0.5): ') or 0.5)

    for _ in range(values_number):
        x = random()
        yield (1 - exp(-_lambda * x)) if x > 0 else 0
```

First 10 values distributed exponentially.

```bash
python main.py exp
Input n (default: 10): 10
Input lambda (default: 0.5): 0.5

Results: (0.2499381970303719, 0.03218976226709691, 0.2393197147396946, 0.2451432860755659, 0.3696512538218808, 0.2591434497242815, 0.20007211649649959, 0.10887617175665742, 0.014938490591884679, 0.04104118076990437)
```
