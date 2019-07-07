text = "{0}.txt"
for i in range(2**32):
    myfile = open(text.format(str(i)), "w") 