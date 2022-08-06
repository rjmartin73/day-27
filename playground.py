from typing import Type


def add(*args: int):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n: int | float, **kwargs: int | float) -> int | float:

    if type(n) == int or type(n) == float:
        pass
    else:
        raise TypeError(f"Expected int or float, but got {type(n)} as first arg.")
    for (key, val) in kwargs.items():
        if type(val) == int or type(val) == float:
            continue
        else:
            raise TypeError(f"Expected int, got {type(val)} in \"{key}\" instead.")

    for (key, val) in kwargs.items():
        if key == "multiply":
            n *= val
        elif key == "divide":
            if val == 0:
                raise ZeroDivisionError("Attempt to divide by zero.")
            n /= val
        elif key == "add":
            n += val
        elif key == "minus":
            n -= val
    n = float("{:.2f}".format(n))
    return n


cost = 164.95
tax_rate = 7.25
discount = 20

x = calculate(cost, multiply=tax_rate * .01, add=cost)

print("$", x*2)
