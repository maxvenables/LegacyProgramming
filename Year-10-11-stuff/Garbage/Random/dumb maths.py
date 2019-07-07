al = [(1/2*7),(2*7**-1),(1/2*7**2),(7**3),(7**-4),(7**(2/3)),(7**(-3/2)),(7**4),(7**-3),(7*7**(1/2)),(7**(1/2))]

for i in al:
    for j in al:
        if i == j:
            print(al.index(i), al.index(j))
            
for i in al:
    for j in al:
        for k in al:
            if i * j == k:
                print(al.index(i),al.index(j),al.index(k))
                
for i in al:
    for j in al:
        for k in al:
            for l in al:
                if i * j * k == l and i != k and i != j and i != l and j != k and j != l and l != k:
                    print(al.index(i),al.index(j),al.index(k),al.index(l))