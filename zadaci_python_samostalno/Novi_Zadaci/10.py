# Za danu listu stringova vrati broj stringova iz liste kojima je duljina >=3 i koji imaju barem
# dvije znamenke jednake prvoj znamenci.
# Npr. za listu ['abc', 'aba', 'cc', 'ijki'] će vratiti 2


lista = ['abc', 'aba', 'cc', 'ijki', 'aaa']

brojac = 0

for word in lista:
    pocetnoSlovo = word[0]
    if (len(word) >= 3):
        flag = False
        for slovo in word[1:]:
            if(pocetnoSlovo == slovo):
                flag = True
        if(flag == True):
            brojac += 1
        
print(brojac)
        
