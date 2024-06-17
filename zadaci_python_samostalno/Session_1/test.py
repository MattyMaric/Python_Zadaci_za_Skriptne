def prva_znam(lista):
    br = 0
    def dvije(string):
        b = 0
        for i in range(len(string)):
            if ( string[i] == string[0]):
                b += 1
        return b
    for s in lista:
        if ( len(s) >= 3 and dvije(s) >= 2):
            br += 1
    print(br)
    return  br  

TestLista = ['abc', 'aba', 'cc', 'ijki', 'aaaa']

prva_znam(TestLista)