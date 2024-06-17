def suma_35(n):
    suma = 0
    for num in range(n):
        if (num % 3 == 0 or num % 5 == 0):
            suma = suma + num

    return suma

def broj_znam(n):
    if(n == 0):
        br = 0;

    while(n != 0):
        br = br + 1
        n = n//10

    return br

def najveci_djelitelj(n):
    najdjel = 1;
    for num in range(n):
        if(num % n == 0):
            najdjel = n
        
        return najdjel
    
def sum_znam(n):
    suma = 0

    while(n != 0):
        dodaj = n % 10
        suma = suma + dodaj
        n = n//10

    return suma

def zamjena(n):
    n = int (str(n)[ ::-1] )
    
    return n
