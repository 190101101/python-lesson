import shutil
import zipfile
import os

p1 = zipfile.ZipFile('files/2.zip', 'r')



shutil.make_archive('files/newfiles', 'zip', 'files')