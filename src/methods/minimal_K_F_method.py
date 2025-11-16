from service import M_Plus_N_Minus_1

def minimal_K_F_method(matrix_goods, matrix, n, m, sellers, buyers):
    """Решает тренспортную задачу методом северо-западного угла"""

    sellers_tmp = sellers.copy()
    buyers_tmp = buyers.copy()
    min_k = 10000000000000000000
    max_k = -1111111111111111111
    for i in range(n):
        for j in range(m):
            if matrix[i][j] is not None:
                if matrix[i][j] < min_k:
                    min_k = matrix[i][j]
                if matrix[i][j] > max_k:
                    max_k = matrix[i][j]

    for k in range(min_k, max_k+1):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == k:
                    tmp = min(sellers_tmp[i], buyers_tmp[j])
                    matrix_goods[i][j] = tmp
                    sellers_tmp[i] -= tmp
                    buyers_tmp[j] -= tmp

            if matrix[i][j] is None:
                matrix_goods[i][j] = sellers_tmp[i]

    for i in range(n):
        for j in range(m):
            if matrix_goods[i][j] == 0:
                matrix_goods[i][j] = None

    if not M_Plus_N_Minus_1(matrix_goods, n, m):
        for k in range(min_k, max_k + 1):
            for i in range(n):
                for j in range(m):
                    if matrix[i][j] == k and matrix_goods[i][j] is None:
                        matrix_goods[i][j] = 0
                        return matrix_goods

    return matrix_goods