import random
from pprint import pprint


def podziel(x, y):
    return x / y

def dodaj_i_zaokraglij(x, y, dokladnosc=7):
    # return x + y
    return round(x + y, 7)

if __name__ == '__main__':
    lista_wartosci = []
    for _ in range(10):
        x = random.randint(1, 100)
        y = random.randint(1, 100)

        lista_wartosci.append([[x, y], podziel(x, y)])
    pprint(lista_wartosci)