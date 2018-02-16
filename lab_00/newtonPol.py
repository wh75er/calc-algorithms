# Newton polynomial interpolation

import os


def func(x):
    return x**3/3


def tableInit(n):
    x = []
    y = []
    for i in range(n):
        x.append(i)
        y.append(func(i))

    return x, y

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


def polinomialValues(xIn, yIn, n, k):
    x, y = parsCord(xIn, yIn, 100, k, n)
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
        if(n <= 1):
            break

    f += f2

    return f


def rootFind(x, y, n):
    l, r = map(float, input("Please, input left and right borders with root sep. by spaces: ").split())
    if(polinomialValues(x, y, n, l) * polinomialValues(x, y, n, r) > 0):
        return "err"
    eps = 0.000001
    root = 1
    while(abs(r - l) > eps and root != 0):
        z = l + abs((r - l))/2
        
        if(polinomialValues(x, y, n, z) == 0.0):
            break

        if(polinomialValues(x, y, n, l) * polinomialValues(x, y, n, z) < 0):
            r = z
        elif(polinomialValues(x, y, n, z) * polinomialValues(x, y, n, r) < 0):
            l = z

    return z


def printToFile(x, y):
    f = open("table", "w")
    for i in range(len(x)):        
        s = str("\t" + "{:.3f}".format(x[i]) + "\t\t" + "{:.3f}".format(y[i]) + "\n")
        f.write(s)

    f.close()
    


def main():
    n, k = inputData() #n - polinomial order
    x, y = tableInit(100)

    root = polinomialValues(x, y, n, k)

    print("\nf(x) where x is {} = {:.2f}".format(k, root))
    print("Accurate value is {:.2f}".format(func(k)), end = '\n\n')

#--------------------------------------------------------------------------------------
    
    res = rootFind(x, y, n)

    if (res == "err"):
        print("Roots is not exist"); 
    else:
        print("Root is located in {:.3f}".format(res))


main()
