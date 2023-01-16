import platform

print(platform.platform())
print(platform.architecture())
print(platform.machine())
print(platform.system())

import sys

paths = sys.path

for i in paths:
	print(i)

import random as rnd

print(rnd.random())