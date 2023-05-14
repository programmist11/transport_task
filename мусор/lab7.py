import string


def input_terminals() -> list:
    while True:
        terminals_list = input("Введите терминалы: ").split(' ')
        len_terminals_list = len(terminals_list)
        counter_len_alpha = 0
        counter_len_digit = 0
        for i in terminals_list:
            if i.islower() or i in string.punctuation:
                counter_len_alpha += 1
            if i.isdigit() or i in string.punctuation:
                counter_len_digit += 1
        if counter_len_alpha == len_terminals_list:
            break
        if counter_len_digit == len_terminals_list:
            break
        print(terminals_list)
    return terminals_list


terminals = input_terminals()


def input_non_terminals() -> list:
    while True:
        non_terminals_list = input("Введите нетерминалы: ").split(' ')
        counter_len = 0
        len_non_terminals_list = len(non_terminals_list)
        for i in non_terminals_list:
            if i.isalpha() and i.isupper():
                counter_len += 1
        if counter_len == len_non_terminals_list:
            break
        print(non_terminals_list)
    return non_terminals_list


non_terminals = input_non_terminals()


def input_regulations(list_terminal: list, list_non_terminal: list) -> list:
    list_with_terminal_and_non_terminal = list_terminal + list_non_terminal
    list_with_terminal_and_non_terminal.append('E')
    count_1 = 0
    while True:
        regulations_list = input("Введите правила: ").split(';')
        for i in regulations_list:
            list_i = i.split('->')

            len_list_i0 = len(list_i[0])
            counter_i0 = 0

            len_list_i1 = len(list_i[1])
            counter_i1 = 0

            for j in list_with_terminal_and_non_terminal:
                if j in list_i[0]:
                    counter_i0 += list_i[0].count(j)
                if j in list_i[1]:
                    counter_i1 += list_i[1].count(j)
            if counter_i0 == len_list_i0 and counter_i1 == len_list_i1:
                count_1 += 1
        if count_1 == len(regulations_list):
            break
        print(regulations_list)
    return regulations_list

# тип 1 КЗ
# 0 1 2
# T S
# S->2T2;T->010;T->010T

# тип 3 право-линейный
#a b
#S A B
#S->aA;A->bB;B->b

# тип 1
# Введите терминалы: a b c
# Введите нетерминалы: A B C S
# Введите правила: S->aBCa;BC->CB;C->c;B->b

# тип 0
# Введите терминалы: a
# Введите нетерминалы: S
# Введите правила: S->aS;aS->a


regulations = input_regulations(terminals, non_terminals)
print(regulations)


def grammar_type(regulate: list, terminal: list, non_terminal: list):
    mass = [0, 0, 0, 0]
    len_regulations = len(regulate)
    """3 тип"""
    counter_for_non_terminal = 0
    for i in regulate:
        list_i = i.split('->')
        if list_i[0] in non_terminal and len(list_i[0]) == 1:
            counter_for_non_terminal += 1
    counter_left = 0
    counter_right = 0
    counter_all_left_or_right = 0
    if counter_for_non_terminal == len_regulations:
        for i in regulate:
            list_i = i.split('->')
            if len(list_i[1]) > 2:
                counter_all_left_or_right += 1
                i_1 = list_i[1]
                if i_1[0] in non_terminal and i_1[1] in non_terminal and i_1[1:] in terminal:
                    counter_left += 1
                    mass[3] = 1
                if i_1[-1] in non_terminal and i_1[-2] in non_terminal and i_1[:len(i_1)-1] in terminal:
                    counter_right += 1
                    mass[3] = 1
            elif len(list_i[1]) == 2:
                counter_all_left_or_right += 1
                i_1 = list_i[1]
                if i_1[0] in non_terminal and i_1[1] in terminal:
                    counter_left += 1
                    mass[3] = 1
                if i_1[-1] in non_terminal and i_1[-2] in terminal:
                    counter_right += 1
                    mass[3] = 1
            else:
                counter_all_left_or_right += 1
                i_1 = list_i[1]
                if i_1[0] in terminal:
                    mass[3] = 1
                    counter_left += 1
                    counter_right += 1
        if counter_right == counter_all_left_or_right:
            return '3 тип: право-линейный'
        if counter_left == counter_all_left_or_right:
            return '3 тип: лево-линейный'
    """2 тип"""
    counter_for_non_terminal = 0
    for i in regulate:
        list_i = i.split('->')
        if list_i[0] in non_terminal and len(list_i[0]) == 1:
            counter_for_non_terminal += 1

    if counter_for_non_terminal == len_regulations:
        # try:
        for i in regulate:
            counter_for_lower_and_upper = 0
            list_i = i.split('->')
            i_1 = list_i[1]
            i_0 = list_i[0]
            if 'E' in i_1:
                continue
            if len(i_1) > 2:
                # a = 0
                # b = 0
                # for j in range(len(i_1)):
                #     if i_1[j] in non_terminal:
                #         a = 1
                #     else:
                #         b = 1

                if len(i_0) == 1:
                    return '2 тип: КС'

                if i_1[0] in non_terminal and i_1[1:] in terminal:
                    counter_for_lower_and_upper += 1
                if i_1[0] in terminal and i_1[1:] in non_terminal:
                    counter_for_lower_and_upper += 1
                if counter_for_lower_and_upper:
                    return '2 тип: КС'
                # if a==1 and b==1:
                #     return '2 тип: КС'

        # except IndexError:
        #     return '2 тип: КС'
    """0 тип"""
    counter_for_non_terminal = 0
    for i in regulate:
        list_i = i.split('->')
        for j in list_i[0]:
            if j in non_terminal:
                counter_for_non_terminal += 1
    if counter_for_non_terminal:
        for i in regulate:
            list_i = i.split('->')
            i_1 = list_i[1]
            i_0 = list_i[0]
            if len(i_0) > len(i_1):
                return 'Тип 0'
    return 'Тип 1: КЗ'


print(grammar_type(regulations, terminals, non_terminals))
