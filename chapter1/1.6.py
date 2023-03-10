pairs = [('a', 1), ('a', 2), ('b', 2)]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
d[key].append(value)
print(d)


from collections import defaultdict
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d['a'])