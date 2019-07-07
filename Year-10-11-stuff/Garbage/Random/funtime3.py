def makeCopy(xs):
    xs1 = []
    if "a" in xs:
        xs1.append("a")
    if "b" in xs:
        xs1.append("b")
    if "c" in xs:
        xs1.append("c")
    if "d" in xs:
        xs1.append("d")
    if "h" in xs:
        xs1.append("h")
    return xs1

cs = 0
ds = 0
total = 0
for i in range(5):
    xs = ["a","b","c","d","h"]
    #a
    xs.pop(i)
    for j in range(4):
        xs1 = makeCopy(xs)
        #b
        if "b" in xs1:
            pop = xs1.index("b")
            xs1.pop(pop)
        else:
            xs1.pop(j)
        for k in range(3):
            xs2 = makeCopy(xs1)
            #c
            if "c" in xs2:
                pop = xs2.index("c")
                xs2.pop(pop)
                cs += 2
            else:
                xs2.pop(k)
            for l in range(2):
                xs3 = makeCopy(xs2)
                if "d" in xs3:
                    pop = xs3.index("d")
                    xs3.pop(pop)
                    ds += 1
                elif "h" in xs3:
                    xs3.pop(0)
                else:
                    xs3.pop(l)
                total += 1 
                
print(float(cs)/float(total))
print(float(ds)/float(total))
                    
                    
            
            
            