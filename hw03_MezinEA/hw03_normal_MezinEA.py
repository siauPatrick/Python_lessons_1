__name__ = "Мезин Евгений Александрович"

print('\n\n Задача №1 ')
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """
    Допущение на понимание мною задачи было таким, что n и m - это
    ПОРЯДКОВЫЕ НОМЕРА - ЦИФР, А не их значения.
    """
    fibonachi_list = [1, 1]

    for i in range(2, m):
        fibonachi_list.append(fibonachi_list[i-2]+fibonachi_list[i-1])
    print(f'Список фибоначи начиная с позиции №{n} до позиции {m} - {fibonachi_list[n-1:]} \n')


n = int(input('Введите номер первого числа из ряда Фибоначи: '))
m = int(input('Введите номер второго числа из ряда Фибоначи: '))

fibonacci(n, m)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('\n\n Задача №2 ')
def sort_to_max(origin_list):
    min = origin_list[0]
    list_len = len(origin_list)
    idx_next_min = 0
    bool_sort = True

    while bool_sort:
        idx = 0
        for i in origin_list:
            if i <= origin_list[idx]:
                if idx == list_len:
                    bool_sort = False
                else:
                    idx += 1

            else:
                origin_list.insert(idx, i)
                del origin_list[idx+1]


origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0, -100, 100, 0, -111, 0.123412]
print(f'\nПервоначальный список - {origin_list}')
origin_list.sort()
print(f'Отсортированный волшебным способом список - {origin_list}\n')


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


print('\n\n Задача №3 ')
def my_filter(arg):
    new_list = []
    for i in arg:
        if i > 0:                       # Данное услвие - это условие фильтра
            new_list.append(i)
    return new_list

list1 = [a for a in range(-5, 5)]
print(list1)

print(my_filter(list1))



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


print('\n\n Задача №4 ')
new_dict = {
    1: (1, 1),  # Координаты точки А1
    2: (3, 5),  # Координаты точки А2
    3: (10, 5), # Координаты точки А3
    4: (8, 1)   # Координаты точки А4
}

def check_parallelogram (dict):
        vektor_list = []

        for i in range(1,4):
            vektor_list.append([dict[i+1][0] - dict[i][0], dict[i+1][1] - dict[i][1]])
        vektor_list.append([dict[1][0] - dict[4][0], dict[1][1] - dict[4][1]])

        print(f'Указанные точки образуют следующие вектора: {vektor_list}')


        if (vektor_list[0][0] == -(vektor_list[2][0])) and (vektor_list[0][1] == -(vektor_list[2][1])):
             print('Да!!! Это параллелограмммм')
        else:
            print('Что то пошло не так....это просто 4ре точки')

print(f'Были заданы следущие точки: {new_dict}')
check_parallelogram(new_dict)