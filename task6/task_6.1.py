import sys
import time


t = int(input("Enter "))
while t > 0:
    time.sleep(t)
    t = int(input("Enter "))
else:
    sys.exit()


