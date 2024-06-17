def prva_znam(lista): #Netocno
    br = 0
    brojac = 0
    for rijec in lista:
        if(len(rijec) > 3):
            for slovo in range(len(rijec)):
                if(rijec[slovo] == rijec[0]):
                    brojac += 1

                if (brojac >= 2):
                    br += 1
    return br

def obrnuto(lista):
    novaLista = []
    for rijec in lista:
        novaLista.append(rijec)
        novaLista.append(rijec[::-1])

    return novaLista

def spoj(lista1, lista2):
    novaLista = lista1 + lista2
    novaLista.sort()
    return novaLista

def sortprod(lista):
    def prod(elem):
        return elem[0] * elem[-1]
    lista.sort(key = prod)
    return lista



