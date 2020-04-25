# Queueing Theory Course

Tasks for getting credit.

## Task 1

Poisson distribution with parameters n, lambda and t:

```Python
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
```

First 10 values with lambda = 0.5:

```bash
python main.py poisson
Input n (default: 10): 10
Input lambda (default: 0.5): 0.5
Input t (default: 1): 1

Results: (0.6065306597126334, 0.3032653298563167, 0.07581633246407918, 0.012636055410679864, 0.001579506926334983, 0.0001579506926334983, 1.316255771945819e-05, 9.401826942470136e-07, 5.876141839043835e-08, 3.2645232439132415e-09)
```


## Task 2

Exponential distribution with parameters n and lambda:

```Python
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
```

## Task 3

First 10 values distributed exponentially.

```bash
python main.py exp
Input n (default: 10): 10
Input lambda (default: 0.5): 0.5

Results: (0, 0.3934693402873666, 0.6321205588285577, 0.7768698398515702, 0.8646647167633873, 0.9179150013761012, 0.950212931632136, 0.9698026165776815, 0.9816843611112658, 0.9888910034617577)
```
