import random
name = input("Input the name of your file ")
length = int(input("Input the legnth of you file "))
width = int(input("Input the width of you file "))
text = "{0}.pbn"
myfile = open(text.format(name), "w")
myfile.write("P3\n")
moretext = "{0} {1}"
myfile.write(moretext.format(length, width) + "\n" )
atext = "{0} {1} {2}    "#


for i in range(length):
    for i in range(width):
        color1 = random.randint(0,255)
        color2 = random.randint(0,255)
        color3 = random.randint(0,255)
        myfile.write(atext.format(color1, color2, color3))
    myfile.write("\n")