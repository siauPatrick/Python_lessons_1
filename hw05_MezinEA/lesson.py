import sys
import os
from pprint import pprint

pprint(sys.path)
print(os.name)
os.chdir('../')
print(os.getcwd())

try:
    os.mkdir('new_dir')
except FileExistsError:
    print('Уже есть')