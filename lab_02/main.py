# Newton polynomial interpolation

import os


def func(x, y):
    return x**2+y**2


def tableInit(n):
    a = []
    for i in range(n+1):
        b = []
        for j in range(n+1):
            b.append(func(i, j))
        a.append(b)

    return a


def parsCord(x, y, n, k, order):
    cls = 0
    minim = abs(k - x[0])
    for i in range(n):
        if(abs(k - i) < minim):
            minim = abs(k - i)
            cls = i

    if(cls >= n - order):
        x = x[n-order:]
        y = y[n-order:]
    else:
        x = x[cls:]
        y = y[cls:]

    return x,y

        
    



def inputData():
    os.system('clear')

    print("Please, input order of polynomial:", end = ' ')
    order = int(input())
    print("\n"*2)

    k = float(input("Enter the value of unknown x to find f(x): "))
    return order, k


def polinomialValues(x, y, n, k):
    j = 1
    f = y[0]
    f1 = 1; f2 = 0
    while(True):
        p = []
        for i in range(n):
            p.append((y[i+1]-y[i]) / (x[i+j]-x[i]))
            y[i] = p[i]
        
        f1 = 1
        for i in range(j):
            f1 *= (k - x[i])


        f2 += (y[0] * f1)

        n-=1
        j+=1
        if(n <= 0):
            break

    f += f2

    return f



def printTable(a):
    for i in a:
        for j in i:
            print(j, end = "\t")
        print("\n")
    


def main():
    n, k = inputData() #n - polinomial order
    a = tableInit(5)
    printTable(a)

#    x, y = parsCord(xIn, yIn, 100, k, n)
#    root = polinomialValues(x, y, n, k)

#    print("\nf(x) where x is {} = {:.2f}".format(k, root))
#    print("Accurate value is {:.2f}".format(func(k)), end = '\n\n')

#--------------------------------------------------------------------------------------
    

if __name__ == "__main__":
    main()
