def cycle(minimal_matrix, i_j, n, m):

    for i in range(n):
        for j in range(m):
            if i != i_j[0] and j != i_j[1]:
                if minimal_matrix[i][j] is not None:
                    if minimal_matrix[i][i_j[1]] is not None:
                        if minimal_matrix[i_j[0]][j] is not None:
                            print(f"(+){minimal_matrix[i][j]}")
                            print(f"(-){minimal_matrix[i][i_j[1]]}")
                            print(f"(-){minimal_matrix[i_j[0]][j]}")

                            minn = min(minimal_matrix[i][i_j[1]], minimal_matrix[i_j[0]][j])
                            if minimal_matrix[i_j[0]][i_j[1]] is None:
                                minimal_matrix[i_j[0]][i_j[1]] = minn
                                minimal_matrix[i][j] += minn
                            else:
                                minimal_matrix[i_j[0]][i_j[1]] += minn
                                minimal_matrix[i][j] += minn

                            minimal_matrix[i][i_j[1]] -= minn
                            minimal_matrix[i_j[0]][j] -= minn

                            if minimal_matrix[i][i_j[1]] == 0:
                                minimal_matrix[i][i_j[1]] = None
                            if minimal_matrix[i_j[0]][j] == 0:
                                minimal_matrix[i_j[0]][j] = None

                            return minimal_matrix
    pass
