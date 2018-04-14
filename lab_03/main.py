# Spline polinomial

import os
import tableprint as tp



def inputData():
    os.system('clear')

    l, r = map(int, input("Please, input borders, seperated by spaces: ").split())
    print("Please, input step:", end = ' ')
    step = int(input())
    print("\n"*2)

    k = float(input("Enter the value of unknown x to find f(x): "))
    return l, r, step, k


def func(x):
    return x**3


def tableInit(l, r, n):
    x = []
    y = []
    for i in range(l, r+1, n):
        x.append(i)
        y.append(func(i))

    return x, y


def getValues(x, a):
    n = len(x)

    # get step between points
    h = []
    for i in range(n-1): 
        h.append(x[i+1] - x[i])

    A = []
    for i in range(n-1):
        A.append((3./h[i])*(a[i+1]-a[i])-(3./h[i-1])*(a[i] - a[i-1]))

    l, u, z = [0] * (n+1), [0] * n, [0] * (n+1)
    l[0] = 1
    u[0] = 0
    z[0] = 0

    for i in range(1, n-1):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*u[i-1]
        u[i] = h[i]/l[i]
        z[i] = (A[i] - h[i-1]*z[i-1])/l[i]


    b, c, d = [0] * n, [0] * (n+1), [0] * n
    l[n] = 1
    z[n] = 0
    c[n] = 0

    for j in range(n-2, -1, -1):
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3.
        d[j] = (c[j+1] - c[j])/(3*h[j])


    return b, c, d


def getRoot(k, x, a, b, c, d):
    n = len(x)
    j = 0
    minim = abs(k - x[0])
    for i in range(n):
        if(abs(k - x[i]) < minim and k > x[i]):
            minim = abs(k - x[i])
            j = i

    
    return a[j] + b[j]*(k-x[j]) + c[j]*(k-x[j])**2 + d[j]*(k-x[j])**3
    

def buildTable(a, b, c, d):
    n = len(a)
    print(tp.header(['i', 'ai', 'bi', 'ci', 'di'], 10))
    num = 1
    for i in range(1, n-1):
        print(tp.row([num, "{:.3f}".format(a[i]), "{:.3f}".format(b[i]), \
            "{:.3f}".format(c[i]), "{:.3f}".format(d[i-1])], 10))
        num += 1
    print(tp.row([num, "{:.3f}".format(a[n-1]), "{:.3f}".format(b[0]), \
        "{:.3f}".format(c[n-1]), "{:.3f}".format(d[n-1])], 10))
    print(tp.bottom(5, 10))




def main():
    left, right, step, k = inputData()
    x, a = tableInit(left, right, step)
    b, c, d = getValues(x, a)
    root = getRoot(k, x, a, b, c, d)                # get result of interpolation
    buildTable(a, b, c, d)
    print("\nf(x) where x is {} = {:.2f}".format(k, root))
    print("Accurate value is {:.2f}".format(func(k)), end = '\n\n')




if __name__=="__main__":
    main()
