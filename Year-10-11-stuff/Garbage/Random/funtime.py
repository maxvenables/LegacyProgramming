import random

ds = 0
total = 0
for i in range(100000):
    coats = ["a","b","c","d","h"]
    choice = random.randint(0,4)
    coats.pop(choice)
    if "b" in coats:
        pop = coats.index("b")
        coats.pop(pop)
    else:
        choice = random.randint(0,3)
        coats.pop(choice)
        
    if "c" in coats:
        pop = coats.index("c")
        coats.pop(pop)
        #chosen = "c"
    else:
        choice = random.randint(0,2)
        #chosen = coats[choice]
        coats.pop(choice)
        
    if "d" in coats:
        pop = coats.index("d")
        coats.pop(pop)
        chosen = "d"
    elif "h" in coats:
        chosen = coats[0]
        coats.pop(0)
    else:
        choice = random.randint(0,1)
        chosen = coats[choice]
        coats.pop(choice)
    
    if chosen == "d":
        ds += 1
    total+= 1
    print(float(ds) / float(total))