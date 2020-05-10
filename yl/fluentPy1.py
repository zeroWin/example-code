import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
Card1 = collections.namedtuple('Card', ['rank', 'suit', 'haha'])

a = Card(1,2)
b = Card1(1,2,3)
print(type(a))
print(type(b))

