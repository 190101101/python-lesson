import os

#1
cwd = os.getcwd()

scan = os.listdir(cwd)

print(scan)

for i in scan:
	print(i)

print('************')

#2
cwd = os.getcwd()

folder = os.scandir(cwd)

for i in folder:
	print(i)

print('************')


#3
from pathlib import Path

cwd = os.getcwd()
content = Path(cwd)

for i in content.iterdir():
	print(i)

