ds = 0
total = 0
for i in range(0,4):
    coats = ["a","b","c","d","h"]
    #a
    coats.pop(i)
    print(coats)
    coats1 = coats
    if "b" in coats:
        pop = coats1.index("b")
        coats1.pop(pop)
        print(coats1)
    else: 
        for j in range(0,3):
            coats2 = coats1
            coats2.pop(j)
            print(coats2)
            if "c" in coats:
                pop = coats2.index("c")
                coats2.pop(pop)
                print(coats2)
            else:
                for k in range(0,2):
                    coats3 = coats2
                    coats3.pop(k)
                    print(coats3)
                    if "d" in coats:
                        pop = coats3.index("d")
                        coats3.pop(pop)
                        print(coats3)
                        ds += 1
                    elif "h" in coats3:
                        coats3.pop(0)
                        print(coats3)
                    else:
                        for l in range(0,1):
                            coats3.pop(l)
                            print(coats3)
                    total += 1
    
                    
print(float(ds)/float(total))
    
    
    