import pandas as pd
from src.potancial_utils.cycle import cycle
from src.potancial_utils.get_U_V import get_U_V
from src.potancial_utils.is_optimized import is_optimized
from service import add_kf_to_matrix_values, search_cost, copy_mass


def potential_method(minimal_matrix, matrix, n, m, iter):
    """Находим массив U и V"""

    mass_U_V = get_U_V(minimal_matrix, matrix, n, m, 4)
    mass_U = mass_U_V[0]
    mass_V = mass_U_V[1]

    """Проверка на оптимальность возвращает True если опртимизированная в противном случае возвращает индексы элепмента начала цикла"""
    i_j = is_optimized(matrix, mass_U_V, m, n)

    if i_j == True:
        return minimal_matrix

    print(f"Итерация {iter} ", end="\n\n\n")

    mass_V_for_view = [f"V={i}" for i in mass_V]
    mass_U_for_view = [f"U={i}" for i in mass_U]

    minimal_matrix_for_view = copy_mass(minimal_matrix, n, m)
    minimal_matrix_for_view = add_kf_to_matrix_values(minimal_matrix_for_view, matrix, n, m)

    df = pd.DataFrame(minimal_matrix_for_view, columns=mass_V_for_view, index=mass_U_for_view)

    print(df, end="\n\n\n")
    print(f"DELTA {i_j}")

    minimal_matrix = cycle(minimal_matrix, i_j, n, m)

    minimal_matrix_for_view = copy_mass(minimal_matrix, n, m)
    minimal_matrix_for_view = add_kf_to_matrix_values(minimal_matrix_for_view, matrix, n, m)

    df = pd.DataFrame(minimal_matrix_for_view, columns=mass_V_for_view, index=mass_U_for_view)
    print(df, end="\n\n\n")

    print(f"Общая стоимость решения {search_cost(minimal_matrix, matrix, n, m, )}", end="\n\n\n")

    return potential_method(minimal_matrix, matrix, n, m, iter+1)
