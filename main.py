import pandas as pd

from minimal_K_F_method import minimal_K_F_method
from start_raspr_method import start_rasp_method
from service import sum_element
from potential_method import potential_method


# n = int(input("Введите n "))
# m = int(input("Введите m "))
n = 3
m = 5

# sellers = [0]*n
# for i in range(n):
#     sellers[i] = int(input(f"Введите, сколько товара у поставшика {i+1} "))
#
#
# buyers = [0]*m
# for i in range(m):
#     buyers[i] = int(input(f"Введите, сколько товара нужно купить клиенту {i+1} "))

# VLAD
# sellers = [200, 350, 150]
# buyers = [100, 100, 80, 90, 70]

# I AM
sellers = [300, 120, 300]
buyers = [100, 120, 130, 100, 90]

# KHADJI
# sellers = [150, 320, 400]
# buyers = [100, 120, 100, 200, 300]

# KSYSHA
# sellers = [200, 150, 350]
# buyers = [120, 120, 200, 180, 110]



if sum_element(buyers) > sum_element(sellers):
    sellers.append(sum_element(buyers)-sum_element(sellers))
    st = 1
    n += 1
elif sum_element(buyers) < sum_element(sellers):
    buyers.append(sum_element(sellers)-sum_element(buyers))
    st = 2
    m += 1
#
# matrix = [None] * n
# matrix_goods = [None] * n
# for i in range(n):
#     matrix[i] = [None] * m
#     matrix_goods[i] = [None] * m
#
# for i in range(0, n):
#     print(matrix[i])
#
# for i in range(n):
#     for j in range(m):
#         if st == 1:
#             if i+1 == n:
#                 matrix[i][j] = None
#                 continue
#         if st == 2:
#             if j+1 == m:
#                 matrix[i][j] = None
#                 continue
#         matrix[i][j] = int(input(f"Введите коэффицент [{i+1}][{j+1}] "))


# I AM
matrix = [[1, 4, 5, 3, 1, None], [2, 1, 2, 1, 2, None], [3, 1, 4, 2, 1, None]]
# VLAD
# matrix = [[1, 4, 5, 3, 1, None], [2, 3, 1, 4, 2, None], [2, 1, 3, 1, 1, None]]
# KHADJI
# matrix = [[2, 5, 3, 6, 1, None], [1, 1, 4, 4, 2, None], [4, 1, 2, 3, 5, None]]
# KSYSHA
# matrix = [[1, 2, 3, 5, 2], [4, 6, 7, 3, 1], [2, 2, 3, 4, 5], [None, None, None, None, None]]


df = pd.DataFrame(matrix, columns=buyers, index=sellers)

print(df, end="\n\n\n")



# I AM, VLAD, KHADJI
matrix_goods = [[None, None, None, None, None, None], [None, None, None, None, None, None], [None, None, None, None, None, None]]
# KSYSHA
# matrix_goods = [[None, None, None, None, None],  [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]

# df = pd.DataFrame(matrix_goods, columns=buyers, index=sellers)
# print(df, end="\n\n\n\n")



print("======START MATRIX GOOODS========")
start_matrix_goods = start_rasp_method(matrix_goods, n, m, sellers, buyers)
df = pd.DataFrame(start_matrix_goods, columns=buyers, index=sellers)
print(df, end="\n\n\n\n\n")




print("========MINIMAL KF METHOD=========")
minimal_matrix = minimal_K_F_method(start_matrix_goods, matrix, n, m, sellers, buyers)
# northwest_matrix = [[100, None, None, None, 20, 130], [None, 120, None, None, None, 0], [None, None, 130, 100, 70, 70]]
df = pd.DataFrame(minimal_matrix, columns=buyers, index=sellers)
print(df, end="\n\n\n\n\n")




print("======METOD POTANCEVALOV=======")
potential_matrix = potential_method(minimal_matrix, matrix, n, m, 0)
# df = pd.DataFrame(potential_matrix, columns=buyers, index=sellers)
# print(df, end="\n\n\n\n\n")




# df = pd.DataFrame(dance_matrix, columns=buyers, index=sellers)
# print(df, end="\n\n\n\n\n")



