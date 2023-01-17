import os
from pathlib import Path

find = 'C:\\Users\\190101101\\program\\soft'

with Path(find) as folder:
	for file in folder.iterdir():
		if file.is_file() & file.name.endswith('.exe'):
			print(file)
