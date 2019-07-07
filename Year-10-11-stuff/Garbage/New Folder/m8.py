def reverse(word):
    reverseWord = ""
    length = len(word)
    while length != 0:
        reverseWord += word[length-1]
        length -= 1
    return reverseWord

def convertDenToHex(num):
    bin = convertDenToBin(num)
    hexa = convertBinToHex(str(bin))
    return hexa
    
def convertDenToBin(num):
    newString =""
    num = int(num)
    orgNum = num
    zeros = ""
    
    while num != 0:
        littleString = str(num % 2)
        num = num // 2
        newString += littleString
    newString = reverse(newString)
        
    length = len(newString) 
    
    count = 8 - length
    while count > 0:
        zeros += "0"
        count -= 1
    
    final = zeros + newString
    
    return final
    
def convertBinToHex(num):
    hexs = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    bins = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
    final = ""
    counter = 0
    zeroes = ""
    nibbles = ""
    length = 8 - len(num)
    while length > 0:
        zeroes += "0"
        length -= 1
    num = zeroes + num
    for i in str(num):
        nibbles += i
        counter += 1
        if counter == 4:
            indexAt = bins.index(nibbles)    
            final += hexs[indexAt]
            counter = 0
            nibbles = ""
    return final


num = ""
num = str(input("input denary number"))
numOne = int(num[0])
numeTwo = int(num[1])
print(numOne)
print(str(convertDenToHex(numOne)+str(convertDenToHex(numeTwo))))