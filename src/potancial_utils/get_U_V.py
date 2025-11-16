def get_U_V(northwest_matrix, matrix, n, m, iter):
    """Находим массив U и V"""
    mass_u = [0] + [None] * (n-1)
    mass_v = [None] * m

    for k in range(iter):
        for i in range(n):
            for j in range(m):

                if matrix[i][j] == None:
                    matrix[i][j] = 0

                if northwest_matrix[i][j] != None:

                    if mass_v[j] is not None:
                        mass_u[i] = 0
                        mass_u[i] = matrix[i][j] - mass_v[j]
                    if mass_u[i] is None and mass_v[j] is not None:
                        mass_u[i] = 0
                        mass_u[i] = matrix[i][j] - mass_v[j]
                    if mass_v[j] is None and mass_u[i] is not None:
                        mass_v[j] = 0
                        mass_v[j] = matrix[i][j] - mass_u[i]

    mass = []
    mass.append(mass_u)
    mass.append(mass_v)
    return mass

