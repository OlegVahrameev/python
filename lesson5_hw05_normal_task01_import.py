import os

from lesson5_hw05_easy_task01 import make_dir, remove_dir

def util_menu():
    print("Утилита по работе с папками текущей директории")
    print("1. Перейти в папку")
    print("2. Просмотреть содержимое текущей папки")
    print("3. Удалить папку")
    print("4. Создать папку")
    util_input = input("Выберите операцию: ")
    if util_input == "1":
        dir_move_input = input("Введите название папки: ")
        dir_path = os.path.join(os.getcwd(), str(dir_move_input))
        try:
            os.chdir(dir_path)
            folder_path = os.getcwd()
            print("Вы успешно перешли в папку " + folder_path)
        except FileNotFoundError:
            print('Такой папки не существует')
        print("Выберите операцию \n")
        return util_menu()
    if util_input == "2":
        print(os.listdir())
        print("Выберите операцию \n")
        return util_menu()
    if util_input == "3":
        remove_dir()
        print("Вы успешно удалили папки")
        print("Выберите операцию \n")
        return util_menu()
    if util_input == "4":
        make_dir()
        print("Вы успешно создали папки")
        print("Выберите операцию \n")
        return util_menu()
util_menu()