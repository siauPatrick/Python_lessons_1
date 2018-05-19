# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("""
    help - получение справки
    mkdir <dir_name> - создание директории
    rmdir <dir_name> - удаление директории
    cp <file_name> - создает копию указанного файла
    rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
    cd <full_path or relative_path> - меняет текущую директорию на указанную
    ls - отображение полного пути текущей директории
    """)

def mkdir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))


def rmdir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(name))
    except FileNotFoundError:
        print('директория {} не существует'.format(name))


def cp():
    if not name:
        print("Необходимо указать имя копируемого файла вторым параметром")
        return
    new_name = str(name) + '_new'
    try:
        shutil.copy(name, new_name)
        print('копия файла {} создана'.format(name))
    except FileNotFoundError:
        print('файл {} не существует'.format(name))


def rm():
    if not name:
        print("Необходимо указать имя удаляемого файла вторым параметром")
        return
    try:
        conf = input('Вы действительно хотите удалить файл {}? (y/n)'.format(name))
        if conf == 'y':
            os.remove(name)
            print('файл {} удален'.format(name))
        else:
            print('Удаление отменено')
    except FileNotFoundError:
        print('файл {} не существует'.format(name))


def cd():
    if not name:
        print("Необходимо указать относительный путь от текущей папки или "
              "полный путь до директории в которую хотите перейти вторым параметром")
        return
    try:
        os.chdir(name)
        print('Вы в директории {}'.format(name))
    except FileNotFoundError:
        try:
            os.chdir(os.path.join(os.getcwd(), name))
        except FileNotFoundError:
            print('Директория {} не существует'.format(name))


def ls():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": mkdir,
    "cp": cp,
    "rm": rm,
    "rmdir": rmdir,
    "cd": cd,
    "ls": ls
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")