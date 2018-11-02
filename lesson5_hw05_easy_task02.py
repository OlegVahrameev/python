import os

def dir_list():
    print(next(os.walk('.'))[1])
dir_list()