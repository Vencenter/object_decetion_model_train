import os
import shutil

def copy():
    for i in range(2,121):
        shutil.copy("0001.xml",str(i).zfill(4)+".xml")


copy()
