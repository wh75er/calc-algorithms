import random as r


f = open("data.txt", "w")

for i in range(30):
    f.write(str(r.uniform(10, 90)) + " " + str(r.uniform(10,90)) + " " + str(r.uniform(0, 1)) + "\n")
