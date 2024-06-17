def parni_faktorijel(n):
    umnozak = 1

    for i in range(1,n+1):
        if(i % 2 == 0):
            umnozak = umnozak * i

    return umnozak

def kvadratna(a,b,c):
    d = b ** 2 - 4*a*c
    
    if ( d >= 0):
        return True
    
    return False


def najmanji_kvadrat(n):

    for i in range(n):
        kvadrat = i * i
        if(kvadrat > n):
            return n

