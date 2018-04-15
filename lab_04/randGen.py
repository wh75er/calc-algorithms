import random as r

def f(x):
    return x**3+x+12

def write_file():
    f_add = open("data.txt", "w")
    for i in range(20):
        x = -5 + i * 0.5
        # +-7%
        f_add.write("{:0.4f} {:0.4f} {:0.4f}\n".format(x, f(x) * (1 + (r.random() - 5.7) *
0.1), 1))
    return

if __name__ == "__main__":
    write_file()
