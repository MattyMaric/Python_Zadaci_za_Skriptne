#Napisi program koji ispisuje cjelobrojne elemente koji se pojavljuju 3 ili vise puta unutar
#liste. Generiraj listu od 100 elemenata u rasponu vrijednosti od 0 do 30. 

import random
random_list = [random.randint(0,30) for _ in range(100)]

broj_elemenata = {}

for element in random_list:
    if element in broj_elemenata:
        broj_elemenata[element] += 1
    else:
        broj_elemenata[element] = 1

cesti_elementi = [element for element, count in broj_elemenata.items() if count >= 3]

print("Generirana lista: ", random_list)
print("Elementi koji se pojavljuju 3 ili vise puta ", cesti_elementi)