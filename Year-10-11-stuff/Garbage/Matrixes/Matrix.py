import sys
import random
class styles:
    Green = '\033[92m'
while True:
    newnum = random.randint(0,9)
    nxt = (styles.Green + str(newnum))
    print(nxt, end="")