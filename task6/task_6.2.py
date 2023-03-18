import time
import random


p = time.time()
t = random.randint(0, 100)
while t < 100000:
    t += 1
    print(t)
oper_time = time.time() - p

filename = time.strftime('%H-%M-%S_%d-%m-%Y')
with open(filename + ".txt", "w") as f:
    f.writelines(str(oper_time))
    f.write("\n")
