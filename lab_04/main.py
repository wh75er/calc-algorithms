

def inputData():
    f = open("data.txt", "r");

    order = int(input("Please, input polinomial order: "))

    x = []
    y = []
    weights = []
    for i in f:
        print(i)
        a, b, c = i.split()
        x.append(float(a))
        y.append(float(b))
        weights.append(float(c))

    return x, y, weights, order


def main():
    x, y, weights, order = inputData();
    print(x, y, weights, order);


if __name__ == "__main__":
    main()
