"""改变对象的字符串显示"""


class Pair:
    """如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出。"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # 0表示self，0.x就是self.x
        # !r表示repr()
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        # !s表示str()
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
print(p)
p1 = Pair('a', '4')
print(p1)
print(repr('a'))
print(str('a'))