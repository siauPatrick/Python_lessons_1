import re

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

print('\n Задание №1')

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# решение через генератор - не воплне соответствует примеру, но все равно интересно было))

sm_char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n','o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cap_char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O',
                 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

line_list = [i for i in line if any(i == el for el in sm_char_list)]
print('первый не корректный:) - ', line_list)

# решение с более сложным условием, соответствующее заданию

def compare(char):
    global cap_char_list

    for el in cap_char_list:
        if char == el:
            return
    else:
        return(char)

new_list = ['',]
j = 0

for i in range(len(line)):
    if compare(line[i]) != None:
        new_list[j] = new_list[j] + line[i]
    else:
        new_list.append('')
        j += 1
new_list = [i for i in new_list if i != '']

print('Второй способ - ', new_list)

# решение с регуляркой :)

rex = re.compile(r'([a-z]+)')
print('Третий способ - ', rex.findall(line))



# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

print('\n Задание №2')

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


print(line)
# c использованием RE

rex_2 = re.compile(r'[a-z]{2}([A-Z]+)[A-Z]{2}')
print('Решение 2.1 - ', rex_2.findall(line_2))

# без такового

"""
не понимаю где ошибка в модуле...в принципе работает при обработке последовательности NOGI возвращает 
только N, хотя при дальнейшем срабатывает и на длинных последовательностях.
"""
def compare2(char):
    global cap_char_list

    for el in cap_char_list:
        if char == el:
            return(char)
    else:
        return('+')

new_list = ['',]
j = 0

for i in range(len(line_2)-2):
    if compare2(line_2[i]) != '+':
        if (compare2(line_2[i-1]) == '+' and compare2(line_2[i-2]) == '+'):
            while (compare2(line_2[i+1]) != '+' and compare2(line_2[i+2]) != '+'):
                new_list[j] = new_list[j] + line_2[i]
                i += 1
    else:
        new_list.append('')
        j += 1

new_list = [i for i in new_list if i != '']

print('Решение 2.2 - ', new_list)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

"""
Задание сделано с допущением, что может НЕ быть САМОЙ Длинной последовательности, т.к. зачастую
существуют несколько совпадений разных цифр в разных местах числа. По этому вывод осуществляется 
списком с указанием количества повторов цифр из списка

"""

print('\n Задание №3')

import os
import random

numb_list = [str(random.randint(0, 9)) for i in range(250000)]
big_munb = ''.join(numb_list)

dir = 'Data'
file = open(os.path.join(dir, 'big_number.txt'), 'w', encoding='utf-8')
file.write(big_munb)
file.close()

file = open(os.path.join(dir, 'big_number.txt'), 'r', encoding='utf-8')
num_from_file = file.read()

list_of_regex = []
longest_line =[]
wet_regex = r'(.)'
repeat = '\\1'
rep_count = 1

while True:
    wet_regex = wet_regex + repeat
    regex = re.compile(wet_regex)
    list_of_regex = regex.findall(num_from_file)
    if list_of_regex == []:
        break
    else:
        longest_line = list_of_regex
        rep_count += 1
print(num_from_file)
print(f'Цифры в данном списке {longest_line} повторяются по {rep_count} раз')
