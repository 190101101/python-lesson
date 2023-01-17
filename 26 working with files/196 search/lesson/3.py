import os
from pathlib import Path
import fnmatch

find = 'C:\\Users\\190101101\\program\\soft'

ext = '*.exe'
with Path(find) as folder:
	for file in folder.iterdir():
		if file.is_file() & fnmatch.fnmatch(file.name, ext):
			print(file.name)

