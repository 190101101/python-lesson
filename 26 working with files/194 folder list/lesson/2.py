import os

# file = 'C:\\Users\\190101101\\dev\\python\\base\\26 working with files\\194 folder list\\lesson\\note'
cwd = os.getcwd()
scan = os.listdir(cwd)

#1
for cw in scan:
	if os.path.isfile(cw):
		print(cw)

print('********')

#2
with os.scandir(cwd) as cwds:
	for cw in cwds:
		if cw.is_file():
			print(cw)


print('********')

#3			
folder = os.scandir(cwd)
for element in folder:
	if element.is_file():
		print(element)

print('********')

from pathlib import Path

folder = Path(cwd)
files = folder.iterdir()

for file in files:
	if file.is_file():
		print(file)