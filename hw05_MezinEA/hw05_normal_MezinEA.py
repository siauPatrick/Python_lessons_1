import hw05_modul_normal as myconsole
import sys


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def help():
    print("""
    help - вывод этой справки
    chenge_dir - сменить папку
    look_dir - посмотреть её содержимое
    create_dir - создать новую папку
    remove_dir - удалить папку
    """)


do = {
    'help': help,
    'change_dir' :  myconsole.change_dir,
    'look_dir' : myconsole.look_dir,
    'create_dir' : myconsole.create_dir,
    'remove_dir' : myconsole.remove_dir
}

if __name__ == '__main__':
    command = sys.argv[1]
    if command in do:
        try:
            arg = sys.argv[2]
            do[command](arg)
        except IndexError:
            do[command]()
    else:
        help()
