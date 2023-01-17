import os, shutil
from pathlib import Path

f1 = 'f1/file.txt'
f2 = 'f1/file2.txt'
shutil.copy(f1, f2)