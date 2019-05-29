from math import *
import numpy as np
import matplotlib.pyplot as plt
import copy

def f(x, j):
    return pow(x, j)

def approximate(x, coefs):
    y = 0
    for j in range(n + 1):
        y += coefs[j] * f(x, j)
        
    return y

def nparray_to_list(a):
    a = list(a)
    for i in range(len(a)):
        a[i] = list(a[i])
    return a

def gauss_seidel(A, b, eps):
    n = len(A)  
    x = [0 for i in range(n)]

    converge = False
    while not converge:
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new
    return x

def solve():
    N = len(x)
    A = np.zeros((n + 1, n + 1))
    B = np.zeros((n + 1, 1))
    for j in range(n + 1):
        for k in range(n + 1):
            for i in range(N):
                A[j, k] += f(x[i], k + j) * p[i]
        for i in range(N):
            B[j] += y[i] * f(x[i], j) * p[i]

    det = np.linalg.det(A)
    
    nparray_to_list(A)
    nparray_to_list(B)
    
    print("determinant: ", det)
    if abs(det) <= 1e-7:
        print("\nDeterminant is NULL!\n")
        exit()

    return gauss_seidel(A, B, 1e-4)



x = []
y = []
p = []

with open("data.txt", "r") as file:
    for line in file.readlines():
        line = line.split()
        if len(line) != 3:
            continue
        else:
            x.append(float(line[0]))
            y.append(float(line[1]))
            p.append(float(line[2]))

if len(x) == 0:
    print("Table is NULL!Error\n")
    exit()
else:
    print("Table with len ", len(x), ":")
    print('x          |       y    |        weights')
    print('-'*40)
    for i in range(len(x)):
        print('{:>10.5f} | {:>10.5f} | {:>10.5f}'.format(x[i], y[i], p[i]))
    print()
    
n = int(input('input polinomial order: '))

coefs = solve()


x_show = [min(x) - (max(x) - min(x)) / 10 + i * 1.2 * (max(x) - min(x)) / 1000 for i in range(1000)]
plt.plot(x, y, 'ko')
plt.plot(x_show, [approximate(i, coefs) for i in x_show], '-r')

plt.show()
