text = "{0}.txt"
import os
i = 0
while True:
    os.remove(text.format(str(i)))
    i += 1