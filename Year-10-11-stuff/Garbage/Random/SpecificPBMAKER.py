#wot in tarnationdef hexadecimal_to_denary(hexadecimal_no):
    den_no = 0
    hexlist = []
    for i in range(len(hexadecimal_no)):
        hexlist.append(hexadecimal_no[i])
        if hexlist[i] == "A":
            hexlist[i] = "10"
        elif hexlist[i] == "B":
            hexlist[i] = "11"
        elif hexlist[i] == "C":
            hexlist[i] = "12"
        elif hexlist[i] == "D":
            hexlist[i] = "13"
        elif hexlist[i] == "E":
            hexlist[i] = "14"
        elif hexlist[i] == "F":
            hexlist[i] = "15"
        else:
            hexlist[i] = hexlist[i]
        place_value = 16**((len(hexadecimal_no)-i) - 1)
        den_no = den_no + int(hexlist[i]) * place_value
    return den_no

