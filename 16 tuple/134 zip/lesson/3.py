import string

p1 = list(string.ascii_lowercase)
p2 = range(1, 27)
p3 = zip(p1, p2)

for p1, p2 in p3:
	print("from p1: {0}, {1} from p2".format(p1, p2))