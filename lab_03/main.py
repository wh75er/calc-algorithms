# Spline polinomial

import os



def inputData():
    os.system('clear')

    l, r = map(int, input("Please, input borders, seperated by spaces: ").split())
    print("Please, input step:", end = ' ')
    step = int(input())
    print("\n"*2)

    k = float(input("Enter the value of unknown x to find f(x): "))
    return l, r, step, k


def func(x):
    return x**3/3


def tableInit(l, r, n):
    x = []
    y = []
    for i in range(l, r+1, n):
        x.append(i)
        y.append(func(i))

    return x, y


def getValues(x, a):

    # get step between points
    h = []
    for i in range(len(x)-1): h.append(x[i+1] - x[i])

    # find matrix A
    A = [0] * len(x) 
    for i in range(1, len(x)-1): 
        A[i] = (3 * (a[i+1]-a[i]) / h[i] - 3 * (a[i] - a[i-1]) / h[i-1])

    print(len(A))

    # solution for system
    l = [0] * (len(x) + 1)
    u = [0] * (len(x) + 1)
    z = [0] * (len(x) + 1)

    l[0] = 1
    u[0] = 0
    z[0] = 0
    for i in range(1, len(x)-1):
        l[i] = 2 * (x[i+1] - x[i]) - h[i-1] * u[i-1]
        u[i] = h[i]/l[i]
        z[i] = (A[i] - h[i-1] * z[i-1]) / l[i]

    l[len(x)] = 1
    z[len(x)] = 0
    c = [0] * (len(x) + 1)
    c[len(x)] = 0

    # find values
    b = [0] * len(x)
    c = [0] * len(x)
    d = [0] * len(x)
    for j in range(len(x)-1, -1, -1):
        print(j)
        c[j] = z[j] - u[j] * c[j+1]                     # error ocures here
        d[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])

    return b, c, d
    



def main():
    left, right, step, k = inputData()
    x, a = tableInit(left, right, step)
    b, c, d = getValues(x, a)
    print("i\t\tai\t\tbi\t\tci\t\tdi")
    for i in range(len(x)):
        print(i, "\t\t", a[i], "\t\t", b[i], "\t\t", c[i], "\t\t", d[i])
    




if __name__=="__main__":
    main()
