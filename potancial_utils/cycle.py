def cycle(minimal_matrix, matrix, i_j, n, m):
    """"""
    # minimal_matrix_copy = minimal_matrix.copy()

    # print(search_in_right(2, 0, None, minimal_matrix, m))
    # print(search_in_left(2, 5, None, minimal_matrix))
    # print(search_in_down(0, 2, None, minimal_matrix, n))
    # print(search_in_up(0, 0, None, minimal_matrix, n))
    st = [0, 0, 0, 0]

    # for i in range(n):
    #     if minimal_matrix[i][i_j[1]] is not None:

    for i in range(n):
        for j in range(m):
            if i != i_j[0] and j != i_j[1]:
                if minimal_matrix[i][j] is not None:
                    if minimal_matrix[i][i_j[1]] is not None:
                        if minimal_matrix[i_j[0]][j] is not None:
                            print(f"(+){minimal_matrix[i][j]}")
                            print(f"(-){minimal_matrix[i][i_j[1]]}")
                            print(f"(-){minimal_matrix[i_j[0]][j]}")
                            if minimal_matrix[i_j[0]][i_j[1]] is None:
                                minimal_matrix[i_j[0]][i_j[1]] = min(minimal_matrix[i][i_j[1]], minimal_matrix[i_j[0]][j])
                                minimal_matrix[i][j] += min(minimal_matrix[i][i_j[1]], minimal_matrix[i_j[0]][j])
                            else:
                                minimal_matrix[i_j[0]][i_j[1]] += min(minimal_matrix[i][i_j[1]], minimal_matrix[i_j[0]][j])
                                minimal_matrix[i][j] += min(minimal_matrix[i][i_j[1]], minimal_matrix[i_j[0]][j])

                            minn = min(minimal_matrix[i][i_j[1]], minimal_matrix[i_j[0]][j])
                            minimal_matrix[i][i_j[1]] -= minn
                            minimal_matrix[i_j[0]][j] -= minn

                            if minimal_matrix[i][i_j[1]] == 0:
                                minimal_matrix[i][i_j[1]] = None
                            if minimal_matrix[i_j[0]][j] == 0:
                                minimal_matrix[i_j[0]][j] = None

                            return minimal_matrix






    # while True:
        # if search_in_right(i_j[0], i_j[1], None, minimal_matrix, n, m):
        #     st[0] = 1
            # print(f"[{i_j[0]}][{}]")
        # if search_in_left(i_j[0], i_j[1], None, minimal_matrix, n, m):
        #     st[1] = 2
        # if search_in_down(i_j[0], i_j[1], None, minimal_matrix, n, m):
        #     st[2] = 3
        # if search_in_up(i_j[0], i_j[1], None, minimal_matrix, n, m):
        #     i = search_in_up(i_j[0], i_j[1], None, minimal_matrix, n, m)
        #     if search_in_right(i, i_j[1], None, minimal_matrix, n, m):
        #         j = search_in_right(i, i_j[1], None, minimal_matrix, n, m)
        #         if search_in_down(i, j, None, minimal_matrix, n, m):
        #             i = search_in_down(i_j[0], i_j[1], None, minimal_matrix, n, m)
        #             if search_in_left(i_j[0], i_j[1], None, minimal_matrix, n, m):
        #                 j = search_in_left(i_j[0], i_j[1], None, minimal_matrix, n, m)
        #                 print(i, j)


        # print(f"st{st}")
        # break

    pass


# def search_in_right(start_i, start_j, stop, minimal_matrix, n, m):
#     if stop is None:
#         stop = m + 1
#
#     for j in range(start_j+1, stop):
#         if minimal_matrix[start_i][j] is not None:
#             return j
#
#
# def search_in_left(start_i, start_j, stop, minimal_matrix, n, m):
#     if stop is None:
#         stop = 0
#
#     for j in reversed(range(stop, start_j)):
#         if minimal_matrix[start_i][j] is not None:
#             # print(minimal_matrix[start_i][j])
#             return j
#
#
# def search_in_down(start_i, start_j, stop, minimal_matrix, n, m):
#     if stop is None:
#         stop = n + 1
#
#     for i in range(start_i + 1, stop):
#         if minimal_matrix[i][start_j] is not None:
#             # print(minimal_matrix[i][start_j])
#             return i
#
#
# def search_in_up(start_i, start_j, stop, minimal_matrix, n, m):
#     if stop is None:
#         stop = 0
#
#     for i in reversed(range(stop, start_i)):
#         if minimal_matrix[i][start_j] is not None:
#             print(minimal_matrix[i][start_j])
#             return i