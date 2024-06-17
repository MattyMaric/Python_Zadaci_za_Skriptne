# . Napisi program i funkciju loto642 koja simulira loto 6/42.
# a. Funkcija izvlaci 6 brojeva te jedan dopunski broj preko generatora slučajnih
# brojeva. Funkcija vraća listu loto brojeva.
# b. Brojeve igrača možete unijeti prilikom inicijalizacije liste (ručno).
# c. Potrebno je odrediti ukupan broj pogodataka pri izvlačenju i ispisati na ekran.
# d. Odrediti sumu pogođenih, minimum i maksimalni pogođeni broj. 

from random import randint

moji_brojevi = []

for num in range(6):
    broj = int(input("Unesite broj: "))
    moji_brojevi.append(broj)

print(moji_brojevi)


def lotto642(lista):
    loto_brojevi = []
    pogodeniBrojevi = 0
    suma = 0
    max = 0
    min = 43

    for broj in range(20):
        lotoBroj = randint(1,42)
        loto_brojevi.append(lotoBroj)

        for i in lista:
            if(i == lotoBroj):

                suma += lotoBroj
                pogodeniBrojevi += 1

                if(lotoBroj > max):
                    max = lotoBroj

                if(lotoBroj < min):
                    min = lotoBroj

    print(pogodeniBrojevi)
    print(min)
    print(max)
    print(suma)

    print(loto_brojevi)

lotto642(moji_brojevi)
