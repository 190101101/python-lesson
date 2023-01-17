import os, shutil
from pathlib import Path

os.makedirs('f1/f2/f3/f1/f2/f3/f1/f2/f3/f1/f2/f3/f1/f2/f3/f1/f2/f3')
os.makedirs('f1')

shutil.rmtree('f1')
