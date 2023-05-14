import pandas as pd
from potancial_utils.cycle import cycle
from potancial_utils.get_U_V import get_U_V
from potancial_utils.is_optimized import is_optimized


def potential_method(minimal_matrix, matrix, n, m, iter):
    """Находим массив U и V"""
    print(f"Итерация {iter} ", end="\n\n\n")
    mass_U_V = get_U_V(minimal_matrix, matrix, n, m)
    mass_U = mass_U_V[0]
    mass_V = mass_U_V[1]


    """Проверка на оптимальность возвращает True если опртимизированная в противном случае возвращает индексы элепмента начала цикла"""
    i_j = is_optimized(matrix, mass_U_V, m, n)

    if i_j == True:
        return minimal_matrix



    mass_V_for_view = [f"V={i}" for i in mass_V]
    mass_U_for_view = [f"U={i}" for i in mass_U]

    df = pd.DataFrame(minimal_matrix, columns=mass_V_for_view, index=mass_U_for_view)
    print(df, end="\n\n\n")
    print(f"DELTA {i_j}")


    cycle(minimal_matrix ,matrix, i_j, n, m)




    # return potential_method(minimal_matrix, matrix, n, m, iter+1)
    return minimal_matrix