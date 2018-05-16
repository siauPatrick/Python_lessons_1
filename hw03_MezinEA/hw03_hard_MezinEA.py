__name__ = "Мезин Евгений Александрович"

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def check_count(a):
    """
    Данная фунция проверяет на то, что число является дробным,
    т.к. весь поледующий алгоритм требует наличия числителя и знаменателя
    дроби вне зависимости от того, было введено целое число или его
    дробное представление.
    """
    try:
        int(a)
    except:
        return a

    a = a + '/1'
    return a


def check_easy (a, b):
    """
    Данная функция необходима для упрощения числителя или знаменателя, а
    также для выделения целой части дроби.
    """
    whole = 0

    if abs(a) >= abs(b):
        whole = a // b
        if whole < 0:
            whole = whole + 1
        a = abs(a) - abs(whole) * abs(b)

    if a == 0:
        return whole
    else:
        i = abs(a)
        while i >= 1:
            if ((a % i) == 0 and (b % i) == 0):
            # if frac.is_integer:
                a = a / i
                b = b / i
            i -= 1
            if whole == 0:
                answer = str(int(a)) + '/' + str(int(b))
            else:
                answer = str(whole) + ' ' + str(int(a)) + '/' + str(int(b))
        return answer


expression = input('Введите выражение')

# Разбиваем выражение на слагаемые и знак операции
expression_list = expression.split(' ')

# Получаем слагаемые и проверяем, являются ли они дробью
expression_list[0] = check_count(expression_list[0])
expression_list[2] = check_count(expression_list[2])

# Разбиваем дроби на числители и знаменатели и переводим их в числа
x1 = expression_list[0].split('/')
x2 = expression_list[2].split('/')

x1_num = int(x1[0])
x2_num = int(x2[0])
x1_domin = int(x1[1])
x2_domin = int(x2[1])

# Приводим дроби к общему знаменателю
if x1_domin == x2_domin:
    pass
else:
    x1_num = x1_num * x2_domin
    x2_num = x2_num * x1_domin
    x1_domin = x1_domin * x2_domin
    x2_domin = x1_domin

# Определяем складываем или вычитаем числители
if expression_list[1] == "+":
    rez_num = x1_num + x2_num
elif expression_list[1] == "-":
    rez_num = x1_num - x2_num
else:
    print('Такому виду операции меня не научили')

# Упрощаем нашу дробь и выделяем целую часть
print(check_easy(rez_num, x1_domin))





# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


"""
Для начала необходимо открыть файлы и построчно перенести их в списки.
После чего убрать знак окончания строки, вызвав меторд rstrip, а также разбить
строку на целевые слова, при этом исключив лишние пробелы, вызвав процедуру фильтр
Также для удобства в первом цикле формирую пустой список для готового решения, что бы
не создавать генератором, и что бы число "ячеек" было сопоставимо с количеством работников
"""

workers = open('workers.txt')
hours = open('hours_of.txt')

workers_list = []
hours_list = []
salary_list = []

for line in workers:
    workers_list.append(list(filter(lambda x: x != '', line.rstrip('\n').split(' '))))
    salary_list.append([])
workers_list = workers_list[1:]
salary_list = salary_list[1:]

print(workers_list)

for line in hours:
    hours_list.append(list(filter(lambda x: x != '', line.rstrip('\n').split(' '))))
hours_list = hours_list[1:]

print(hours_list)

"""
Циклом формирую список состоящий из Фамилии, Имени и расчетной версии заработной
платы в соответствии с техзаданиемю
Вывожу результат на экра и закрываю файлы.
"""

idx = 0
for i in workers_list:
    for j in hours_list:
        if ((i[0] == j[0]) and (i[1] == j[1])):
            salary_list[idx].append(i[0])
            salary_list[idx].append(i[1])

            if int(j[2]) < int(i[4]):
                salary = int(i[2]) / int(i[4]) * int(j[2])
            else:
                salary = int(i[2]) / int(i[4]) * (int(j[2]) - int(i[4])) * 2 + int(i[2])
            salary_list[idx].append(round(salary, 2))
            idx += 1

print(salary_list)

workers.close()
hours.close()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

fruits = open('fruits.txt', encoding='utf-8', )
fruit_list = []

for line in fruits:
    fruit_list.append(line.strip('\n'))

fruits.close()

fruit_list = list(filter(lambda x: x != '', fruit_list))

first_letter_list = []
for fruit in fruit_list:
    first_letter_list.append(fruit[0])
first_letter_list = set(first_letter_list)
first_letter_list = sorted(first_letter_list)

print(fruit_list)
print(first_letter_list)

for first_letter in first_letter_list:
    name_file = 'fruts_' + first_letter
    file = open(os.path.join('fruts_files', name_file), 'w', encoding='utf-8')
    for fruit in fruit_list:
        if first_letter == fruit[0]:
            file.write(fruit + '\n')
    file.close()