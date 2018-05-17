import sys
import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

for i in range(10):
    name_dir = "dir_" + str(i)
    try:
        os.mkdir(name_dir)
    except FileExistsError:
        pass

input('Check dirs')

for i in range(10):
    name_dir = "dir_" + str(i)
    try:
        os.rmdir(name_dir)
    except FileExistsError:
        pass

print('dirs removed')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(os.getcwd(), ':')
print(os.listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

full_path = str(os.path.realpath(__file__))
dir_and_name = full_path.rpartition('/')

shutil.copy(dir_and_name[2], dir_and_name[2] + '_new')
input('Check copy')
os.remove(dir_and_name[2] + '_new')