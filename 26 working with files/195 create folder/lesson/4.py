import os
from pathlib import Path

cwd = os.getcwd()

p3 = Path('f1/f2/f3')
p3.mkdir(parents=True, exist_ok=True)