#
#
# print('apple')
# print(type(range(10)))
# print(max(1, 2, 4, 2))
#
# print(max(['asdf', '134da', 'dfa1ewfasd', 'fd'], key=len))
#
# for i in enumerate(['asdf', '134da', 'dfa1ewfasd', 'fd']):
#     print(i)


#
#
# def check_name (first_name, second_name):
#     """
#
#     :param first_name:
#     :param second_name:
#     :return:
#     """
#     print(f'{first_name}{second_name}')
#
#
#
# print(list(map(len, ['asdf', '134da', 'dfa1ewfasd', 'fd'])))
#
#
# def first_letter (item):
#     return item[0]
#
# fruits = ['banana', 'apple', 'orange']
#
# print(list(map(first_letter, fruits)))

#
# list = (1, 2, 3)
# print(type(*list))
#
# from itertools import zip_longest
#
#
# print(list(zip_longest(['name', 'weight'], ['Vova', 70, 170])))


# print(list(filter(lambda x: x[0] == 'o', ['a1', 'a2', '2', '3', 'ba', 'v3', 'a1'])))

# file = open('lesson.py', encoding='utf-8')
# lines = file.readlines()
# print(lines)
# file.close()
#

file = open('new.py', 'w', encoding='utf-8')
file.write("file = open('new.py', 'a', encoding='utf-8') \nfile.write('') \nfile.close()")
file.close()