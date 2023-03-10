"""
映射名称到序列元素
"""

from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jones@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr, joined = sub
print(addr, joined)


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total