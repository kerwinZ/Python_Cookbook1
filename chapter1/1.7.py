from collections import OrderedDict
import json


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
print(d)
for key in d:
    print(key, d[key])
od = json.dumps(d)
print(od)

list_test = [
    ('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)
]

list_dict = json.dumps(list_test)
print(list_dict)