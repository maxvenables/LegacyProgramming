a = input()
isString = True
for i in a:
    if not((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
        isString = False
        
print(isString)

