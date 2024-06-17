def krafna(broj):
    if(broj < 10):
        return "Broj krafni: " + str(broj)
    return "Broj krafni: mnogo"

def oba_kraja(s):
    if(len(s) < 2):
        return " "
    return s[:2] + s[-2:]


def fiksni_start(s):
    prvi = s[0]
    novi = prvi
    for slovo in s[1:]:
        if (slovo == prvi):
            novi += prvi
        else:
            novi += slovo

    return novi

def promijesaj(a, b):
    a1 = b[0] + a[1:]
    b1 = a[0] + b[1:]

    return a1 + " " + b1

