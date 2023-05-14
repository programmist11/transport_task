import numpy as np
from scipy.optimize import linprog
import warnings
warnings.filterwarnings('ignore')
def delta(a, b, c, x):
    if a.sum() > b.sum():
        b = np.hstack((b, [a.sum() - b.sum()]))
        c = np.hstack((c, np.zeros(len(a)).reshape(-1, 1)))
    elif a.sum() < b.sum():
        a = np.hstack((a, [b.sum() - a.sum()]))
        c = np.vstack((c, np.zeros(len(b))))

    m = len(a)
    n = len(b)

    u = np.zeros(m)
    v = np.zeros(n)

    for i in range(m):
        for j in range(n):
            if x[i, j] != 0:
                if v[j] != 0:
                    u[i] = c[i, j]-v[j]
                else:
                    v[j] = c[i, j]-u[i]

    delta = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            delta[i, j] = u[i] + v[j] - c[i, j]
    return delta
def prepare(a, b):
    m = len(a)
    n = len(b)
    h = np.diag(np.ones(n))
    v = np.zeros((m, n))
    v[0] = 1
    for i in range(1, m):
        h = np.hstack((h, np.diag(np.ones(n))))
        k = np.zeros((m, n))
        k[i]=1
        v = np.hstack((v, k))
    return np.vstack((h, v)).astype(int), np.hstack((b,a))

def potenz(a_, b_, c_):
    a = np.copy(a_)
    b = np.copy(b_)
    c = np.copy(c_)
    if a.sum() > b.sum():
        b = np.hstack((b, [a.sum() - b.sum()]))
        c = np.hstack((c, np.zeros(len(a)).reshape(-1, 1)))
    elif a.sum() < b.sum():
        a = np.hstack((a, [b.sum() - a.sum()]))
        c = np.vstack((c, np.zeros(len(b))))

    m = len(a)
    n = len(b)
    A_eq, b_eq = prepare(a, b)
    res = linprog(c.reshape(1, -1), A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='simplex')
    return res.x.astype(int).reshape(m, n), res.fun.astype(int)

def sev_zap(a_, b_, c_):
    a = np.copy(a_)
    b = np.copy(b_)
    c = np.copy(c_)
    if a.sum() > b.sum():
        b = np.hstack((b, [a.sum() - b.sum()]))
        c = np.hstack((c, np.zeros(len(a)).reshape(-1, 1)))
    elif a.sum() < b.sum():
        a = np.hstack((a, [b.sum() - a.sum()]))
        c = np.vstack((c, np.zeros(len(b))))

    m = len(a)
    n = len(b)
    i = 0
    j = 0
    funk = 0
    x = np.zeros((m, n), dtype=int)
    while (i<m) and (j<n):
        x_ij = min(a[i], b[j])
        funk += c[i, j]*min(a[i], b[j])
        a[i] -= x_ij
        b[j] -= x_ij
        x[i, j] = x_ij
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            i += 1
            j += 1
    return x, funk

a = np.array([250, 200, 220])
b = np.array([140, 110, 170, 90, 140])

D = np.array([[1, 2, 3, 5, 2],
              [4, 6, 7, 3, 1],
              [3, 2, 3, 4, 5]])

# print('Матрица системы ограничений: \n', prepare(a, b)[0])
x1, funk1 = sev_zap(a, b, D)
print('Метод северо-западного угла: \n', x1)
print('Целевая функция: ', funk1)
print()
x2, funk2 = potenz(a, b, D)
print('Метод потенциалов: \n', x2)
print('Целевая функция: ', funk2)
print()
print('Дельта матрица для метода северо-западного угла: \n', delta(a, b, D, x1))
print()
print('Дельта матрица для метода потенциалов: \n', delta(a, b, D, x2))