p1 = set(['A', 'A', 'B', 'C', 'W'])
p2 = set(['A', 'D', 'B', 'Q', 'B'])

#
print(p1.difference(p2))
print(p2.difference(p1))

#
print(p1.issubset(p2))
print({'D', 'Q'}.issubset(p2))

#
p2 = set(['A', 'B'])
p1 = set(p2)
print(p1)

print(p1.issuperset(p2))
print(p2.issuperset(p1))
print({'A', 'A'}.issuperset(p1))