def is_optimized(matrix, mass_U_V, m, n):
    """Проверка на оптимальность возвращает True если опртимизированная в противном случае возвращает индексы элепмента начала цикла"""

    mass_U = mass_U_V[0]
    mass_V = mass_U_V[1]

    for i in range(n):
        for j in range(m):
            if mass_V[j] + mass_U[i] > matrix[i][j]:
                tmp_i_j = [i, j]
                return tmp_i_j

    return True