from functools import wraps
import random

def bar_tender(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'The drunk person at the bar says, {original_val}'
    return wrapper


def request_drink(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_val = func(*args, **kwargs)
        return f'Hey bartender, get me a {original_val}, STAT'
    return wrapper


@bar_tender
def just_the_bar(txt):
    return txt


@request_drink
def just_the_drink(txt):
    return txt

@bar_tender
@request_drink
def just_saying(txt):
    return txt


if __name__ == "__main__":
    rand_ind = random.randrange(0, 6)
    drinks = ["Beer", "Cider", "vodka soda", "white claw", "wine", "soda", "water"]
    print(just_saying(drinks[rand_ind]))
