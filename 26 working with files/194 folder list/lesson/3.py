import os
from pathlib import Path

file = 'C:\\Users\\190101101\\dev\\python\\base\\26 working with files\\194 folder list\\lesson\\note'
cwd = os.getcwd()
scan = os.listdir(cwd)

for sc in scan:
	if os.path.isfile(sc):
		print(sc)


print('******')


for sc in scan:
	if os.path.isdir(sc):
		print(sc)