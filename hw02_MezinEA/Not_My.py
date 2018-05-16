import os

path = os.path.join()

N = 111

base_house = [['room']*x for x in range(99) for y in range(x)]


house = [list(enumerate(base_house, start=(i+1))) for
         i in range(1)][0]

room = 1
for floor in house:
    for i in range(len(floor[1])):
        floor[1].remove('room')
        floor[1].append(room)
        room += 1

for floor in house:
    for rooms in floor[1]:
        if rooms == N:
            print('Квартира № %s\nЭтаж %s, %s-я слева' %
                  (N, floor[0], floor[1].index(N) + 1))
