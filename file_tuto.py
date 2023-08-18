
import os
import shutil

source = "1065281.ico"
target = "image/1065281.ico"

shutil.copy(source,target)
os.remove(source)