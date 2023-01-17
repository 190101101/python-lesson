import os
from pathlib import Path

cwd = os.getcwd()

#1
os.makedirs('folder1/folder2')

#2
os.makedirs('folder1/folder2', exist_ok=True)
