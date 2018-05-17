import os
import sys


def change_dir(name):
    try:
        os.chdir(name)
        print('Успешно перешел в папку', name)
    except:
        print('Такой папки нет - перейти невозможно')


def look_dir():
    print(os.listdir())


def create_dir(name):
    try:
        os.mkdir(name)
        print('Успешно создал папку', name)
    except:
        print('Такая папка уже существует')


def remove_dir(name):
    try:
        os.rmdir(name)
        print('Успешно удалил папку ', name)
    except:
        print('Такой папки не существует')