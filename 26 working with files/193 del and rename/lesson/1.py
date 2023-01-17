import os

file = 'lorem.txt'
rename = 'lorem2.txt'

os.rename(file, rename)
os.rename(rename, file)
