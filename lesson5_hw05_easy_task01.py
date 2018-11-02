import os

def make_dir():
    i = 1
    while i <= 9:
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Директория уже существует')
        i += 1
make_dir()

def remove_dir():
    i = 1
    while i <= 9:
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print('Директория уже не существует')
        i += 1
remove_dir()
