def suma_35(n):
    suma = 0
    broj = 0

    while(broj < n):
        if(broj % 3 == 0 or broj % 5 == 0):
            suma += broj
        broj += 1

    return suma

def broj_znam(n):
    znam = 0
    n = abs(n)

    if(n == 0):
        return 1
    
    while(n != 0):
        znam += 1
        n = n // 10

    return znam

def najveci_djeljitelj(n):
    nd = 1
    for i in range(2, n):
        if(n % i == 0):
            nd = i
        
    return nd

def sum_znam(n):
    suma = 0
    n = abs(n)

    while(n != 0):
        zznam = n % 10
        suma = suma + zznam
        n = n // 10

    return suma

def zamjena(n):
    n = int(str(n)[::-1])
    return n



def test(func, ulazi, ocekivano):
    ulazi_str = ', '.join(repr(u) for u in ulazi)
    izlazi = func(*ulazi)
    if izlazi == ocekivano:
        prefix = 'OK'
        infix = '='
    else:
        prefix = ' X'
        infix = '!='
    print(' %s %s(%s) = %r %s %r' % (prefix, func.__name__, ulazi_str, izlazi, infix, ocekivano))



def main():
    print('suma_35')
    test(suma_35, (14, ), 45)
    test(suma_35, (5, ), 3)
    test(suma_35, (100, ), 2318)

    print('broj_znam')
    test(broj_znam, (728, ), 3)
    test(broj_znam, (10, ), 2)
    test(broj_znam, (0, ), 1)
    test(broj_znam, (-59, ), 2)

    print('najveci_djeljitelj')
    test(najveci_djeljitelj, (100, ), 50)
    test(najveci_djeljitelj, (97, ), 1)
    test(najveci_djeljitelj, (803, ), 73)

    print('sum_znam')
    test(sum_znam, (728, ), 17)
    test(sum_znam, (10, ), 1)
    test(sum_znam, (0, ), 0)
    test(sum_znam, (-59, ), 14)

    print('zamjena')
    test(zamjena, (728, ), 827)
    test(zamjena, (12345, ), 54321)
    test(zamjena, (276, ), 672)

if __name__ == '__main__':
    main()
