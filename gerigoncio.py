while True:
    palabra = input("Que palabra quieres traducir a gerigoncio?: ")
    lp = []
    cont = 0
    v1 = ""
    v2 = ""
    for l in palabra:    
        lp.append(l)    
        if l == "a":
            v1 = "a"
            v2 = "pa"
        elif l == "e":
            v1 = "e"
            v2 = "pe"
        elif l == "i":
            v1 = "i"
            v2 = "pi"
        elif l == "o":
            v1 = "o"
            v2 = "po"
        elif l == "u":
            v1 = "u"
            v2 = "pu"

        if l == v1:
            lp.insert(cont+1,v2)
            cont += 1    
        cont += 1
    np = ""
    for i in lp:
        np += i
    print(np)
