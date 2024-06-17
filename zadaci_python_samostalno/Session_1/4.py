def glagovanje(s):
    if(len(s) >= 3):
        if(s[-3:] == "ari"):
            s += "ti"
        else:
            s += "ari"
    else:
        return s
    
    return s


def nije_los(s):
    pass

def pred_zad(a,b):
    duljina = len(a)

    if(duljina % 2 == 0):
        pass

def zamjena(s):
    novistring = ""
    for slovo in s:
        if(slovo.isdigit()):
            novistring += "*"
        elif(slovo.isalpha()):
            novistring += "-"
        else:
            novistring += "?"
    return novistring