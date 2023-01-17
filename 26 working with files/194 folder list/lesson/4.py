import os
from pathlib import Path

cwd = os.getcwd()
scan = os.listdir(cwd)

main_file = Path(cwd)
file_content = main_file.iterdir()

for file in file_content:
	if file.is_dir():
		print(file)