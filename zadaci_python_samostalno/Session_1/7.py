def kriz(r,s):
    matrica = []
    if(r%2 == 0):
        br = r // 2 - 1
    else:
        br = r // 2

    for i in range(br):
        if(s % 2):
            broj_1 = 1
        else:
            broj_1 = 2
        broj_0 = (s-broj_1)//2
        matrica.append([0]*broj_0 + [1]*broj_1+[0]*broj_0)
        if(r%2==1):
            m1 = matrica[::-1]
            matrica.append([1]*s)
            matrica = matrica + m1
        else:
            matrica.append([1]*s)
            matrica = matrica + matrica[::-1]

        return matrica