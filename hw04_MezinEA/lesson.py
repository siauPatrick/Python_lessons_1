import re

a = r'[a-z]+@[a-z]+\.(&:ru|org|com)'


regex = re.compile(r'(\d{2})')


print(regex.findall('I was born in 1234'))
print(re.finditer(r'\d{2}', 'I was born in 1234'))


from copy import deepcopy

new_list = [el for el in range(10) if el % 2 == 0]
print(new_list)