# Newton polynomial interpolation

import os
import tableprint as tp
import pdb


def func(x, y):
    return x**2+y**2


def tableInit(n):
    os.system('clear')
    a = []
    for i in range(n+1):
        b = []
        for j in range(n+1):
            b.append(func(i, j))
        a.append(b)

    return a


def parsCord(matrix, n, x, y, orderX, orderY):                   # a - matrix, n - size, x to find, y to find
    xa = list(range(n+1))
    ya = list(range(n+1))
    clsX = 0
    clsY = 0
    minim = abs(x - xa[0])
    for i in range(n+1):
        if(abs(x - i) < minim):
            minim = abs(x - i)
            clsX = i

    minim = abs(y - ya[0])
    for i in range(n+1):
        if(abs(y - i) < minim):
            minim = abs(y - i)
            clsY = i

    if(clsX >= n - orderX):
        xa = xa[n-orderX:]
    else:
        xa = xa[clsX:clsX+orderX+1]

    if(clsY >= n - orderY):
        ya = ya[n-orderY:]
    else:
        ya = ya[clsY:clsY+orderY+1]

    parsedMatrix = matrix[ya[0]:ya[len(ya)-1]+1]
    for i in range(len(parsedMatrix)):
        parsedMatrix[i] = parsedMatrix[i][xa[0]:xa[len(xa)-1]+1]

    return xa, ya, parsedMatrix

        
    



def inputData():

    orderX = int(input("Please, input order of polynomial X: "))
    orderY = int(input("Please, input order of polynomial Y: "))
    print("\n"*2)

    x = float(input("Enter the value of unknown x to find f(x, y): "))
    y = float(input("Enter the value of unknown y to find f(x, y): "))
    print("\n"*2)

    return orderX, orderY, x, y


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



def bilinearValues(xa, ya, x, y, orderX, orderY, matrix):
    # x interpolation
    rootX = []
    for i in range(len(ya)):
        rootX.append(polinomialValues(xa, matrix[i], orderX, x))
    root = polinomialValues(ya, rootX, orderY, y)
    return root



def printTable(a):
#    for i in a:
#        for j in i:
#            print(j, end = "\t")
#        print("\n")
    for i in range(6):
        a[i].insert(0, i)
    print(tp.top(7, 3))
    print(tp.row(["x/y", 0, 1, 2, 3, 4, 5], 3))
    print(tp.bottom(7, 3))
    print("\r", end='\r\r\r')
    tp.table(a, None, '5g', 5, 'fancy_grid')
    
    


def main():
    matrix = tableInit(5)
    printTable(matrix)
    nx, ny, x, y = inputData() #n - polinomial order

    xa, ya, parsedMatrix= parsCord(matrix, 5, x, y, nx, ny)
    root = bilinearValues(xa, ya, x, y, nx, ny, parsedMatrix)

    print("\nf(x, y) where x is {} and y is {} = {:.2f}".format(x, y, root))
    print("Accurate value is {:.2f}".format(func(x, y)), end = '\n\n')

#--------------------------------------------------------------------------------------
    




if __name__ == "__main__":
    main()
