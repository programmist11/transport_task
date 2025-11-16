def M_Plus_N_Minus_1(matrix_goods, n, m):
    k = 0
    for i in range(n):
        for j in range(m):
            if matrix_goods[i][j] is not None:
                k += 1

    return k == m + n - 1


def sum_element(mass):
    """Суммирует элементы массива"""
    sum = 0
    for i in range(len(mass)):
        sum = sum + mass[i]
    return sum



def search_cost(matrix_values, matrix, n, m):
    sum = 0
    for i in range(n):
        for j in range(m):
            if matrix_values[i][j] is not None:
                if matrix[i][j] is not None:
                    sum += matrix_values[i][j] * matrix[i][j]
    return sum

def add_kf_to_matrix_values(matrix_values, matrix, n, m):
    matrix_values_copy = matrix_values[:]
    for i in range(n):
        for j in range(m):
            if matrix_values[i][j] is not None and matrix_values[i][j] != 0:
                matrix_values_copy[i][j] = f"{matrix_values[i][j]}[{matrix[i][j]}]"
                if matrix_values[i][j] is None:
                    matrix_values_copy[i][j] = f"{matrix_values[i][j]}[0]"

    return matrix_values_copy

def copy_mass(mass, n, m):

    mass_copy = [None] * n
    for i in range(n):
        mass_copy[i] = [None] * m

    for i in range(n):
        for j in range(m):
            mass_copy[i][j] = mass[i][j]

    return mass_copy


