"""
从字典中提取子集
"""

import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


@timethis
def get_dict_set():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)

    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    print(p2)

    p3 = dict((key, value) for key, value in prices.items() if value > 200)
    p4 = {key: prices[key] for key in prices.keys() & tech_names}
    print(p3, p4)


if __name__ == '__main__':
    get_dict_set()