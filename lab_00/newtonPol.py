# Newton polynomial interpolation

import os

def inputData():
    os.system('clear')

    print("Please, input order of polynomial:", end = ' ')
    n = int(input())
    print("\n"*2)
    print("Please, input your data, seperated by spaces:") 

    x = []
    y = []
    i = 0
    print("Input node: ")
    print("\tx  |  f(x)")
    while(i < n):
        xIn,yIn = map(float, input("\t").split())
        x.append(xIn)
        y.append(yIn)
        i+=1

    k = int(input("Enter the value of unknown x to find f(x): "))
    return x, y, n, k


def polinomialValues(x, y, n, k):
    j = 1
    f = y[0]
    f1 = 1; f2 = 0
    while(True):
        p = []
        for i in range(n - 1):
            p.append((y[i+1]-y[i]) / (x[i+j]-x[i]))
            y[i] = p[i]
        
        f1 = 1
        for i in range(j):
            f1 *= (k - x[i])


        f2 += (y[0] * f1)

        n-=1
        j+=1
        if(n == 1):
            break

    f += f2

    return f


def main():
    x, y, n, k = inputData()
    root = polinomialValues(x, y, n, k)

    print("f(x) where x is", k, " = ", root)
    


main()
