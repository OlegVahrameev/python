import os

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
        dir_move_input = input("Введите название папки: ")
        dir_path = os.path.join(os.getcwd(), str(dir_move_input))
        try:
            os.rmdir(dir_path)
            print("Вы успешно удалили папку " + dir_path)
        except FileNotFoundError:
            print('Такой папки не существует')
        print("Выберите операцию \n")
        return util_menu()
    if util_input == "4":
        dir_move_input = input("Введите название папки: ")
        dir_path = os.path.join(os.getcwd(), str(dir_move_input))
        try:
            os.mkdir(dir_path)
            print("Вы успешно создали папку " + dir_path)
        except:
            pass
        print("Выберите операцию \n")
        return util_menu()
util_menu()