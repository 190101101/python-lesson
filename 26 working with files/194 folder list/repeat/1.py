import os
from pathlib import Path

cwd = os.getcwd()
scan = os.listdir(cwd)

#1
for cw in scan:
	if os.path.isfile(cw):
		print(cw)
