def isti_kraj(rijeci):
    br = 0
    for r in rijeci:
        if(len(r) >= 2 and (r[0] == r[-1])):
            br += 1

    return br


def izbaci_susjede(lista):
    for broj in lista:
        if(lista[broj] == lista[broj+1]):
            pass