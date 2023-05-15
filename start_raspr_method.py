def start_rasp_method(matrix_goods, n, m, sellers, buyers):
    """Делает стартовое распределение независимое от коэффицентов"""

    sellers_tmp = sellers.copy()
    buyers_tmp = buyers.copy()

    for i in range(n):
        for j in range(m):
            tmp = min(sellers_tmp[i], buyers_tmp[j])
            matrix_goods[i][j] = tmp
            sellers_tmp[i] -= tmp
            buyers_tmp[j] -= tmp

    for i in range(n):
        for j in range(m):
            if matrix_goods[i][j] == 0:
                matrix_goods[i][j] = None

    return matrix_goods