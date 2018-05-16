__name__ = "Мезин Евгений Александрович"

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):

    """
    первая бредовая мысль реализации через строки :))
    работает только с первым вариантом, где нет переходящего округления :)
    """

    # str_number = str(number)
    # list_number = str_number.split('.')
    # dec_count = list_number[1]
    # if int(dec_count[ndigits-1]) >= 5:
    #     round_dig = int(dec_count[ndigits-1]) + 1
    # else:
    #     round_dig = int(dec_count[ndigits-1]) - 1
    # round_dec_count = dec_count[:ndigits-1]
    # round_dec_count = round_dec_count + str(round_dig)
    # return list_number[0]+'.'+round_dec_count


    """
    более корректная математическая реализация
    изначально планировал через остаток, но посчитал, что будет мудренее
    """

    count = number // (10 ** (-ndigits-1))
    round_arg = count % 10
    if round_arg >=5:
        count = count + (10 - round_arg)
    else:
        count = count - round_arg
    return count / (10 ** (ndigits+1))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.999996810328417, 8))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

    # digit_list = str(ticket_number)
    # if len(digit_list) == 6:
    #     idx = 1
    #     first_half = 0
    #     second_half = 0
    #     for i in digit_list:
    #         if idx <=3:
    #             first_half = first_half + int(i)
    #         else:
    #             second_half = second_half + int(i)
    #         idx += 1
    #
    #     if first_half == second_half:
    #        answer = "Билет счастливый"
    #     else:
    #        answer = "Билет не счастливый"
    #     return answer
    # else:
    #     return 'Введен не корректный номер билета'
    #

    """
    Со второго раза родилась более красивая реализация через функционал
    python. Обработка строки - был более деревянным методом
    """

    both_half = divmod(ticket_number,1000)

    half_1 = sum(list(map(int, str(both_half[0]))))
    half_2 = sum(list(map(int, str(both_half[1]))))

    if len(str(ticket_number)) == 6:
        if half_1 == half_2:
            answer = 'ВАМ ПОВЕЗЛО'
        else:
            answer = 'У Вас обычный билет'
    else:
        answer = 'Введена не корректная маска ввода'

    return answer

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
