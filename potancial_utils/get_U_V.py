def get_U_V(northwest_matrix, matrix, n, m):
    """Находим массив U и V"""
    mass_u = [0] + [-999] * (n-1)
    mass_v = [-999] * m

    for k in range(4):
        for i in range(n):
            for j in range(m):

                if matrix[i][j] == None:
                    matrix[i][j] = 0

                if northwest_matrix[i][j] != None:
                    if mass_v[j] != -999:
                        mass_u[i] = 0
                        mass_u[i] = matrix[i][j] - mass_v[j]
                    if mass_u[i] == -999:
                        mass_u[i] = 0
                        mass_u[i] = matrix[i][j] - mass_v[j]
                    if mass_v[j] == -999:
                        mass_v[j] = 0
                        mass_v[j] = matrix[i][j] - mass_u[i]

        for i in range(n):
            for j in range(m):
                if abs(mass_u[i]) > 10:
                    mass_u[i] = -999
                if abs(mass_v[j]) > 10:
                    mass_v[j] = -999

    mass = []
    mass.append(mass_u)
    mass.append(mass_v)
    return mass