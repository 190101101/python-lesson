import os
from pathlib import Path

cwd = os.getcwd()

#1

try:
	os.mkdir('newfolder1')
except FileExistsError as filehave:
	print(filehave)