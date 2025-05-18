# mając dany portfel walutowy:
import threading
import requests

# policzyć jego wartość w złotówkach za pomocą tylu watków ile walut
# w każdym z wątków wysłać zapytnie do API NBP:
# https://api.nbp.pl/api/exchangerates/rates/a/chf/?format=json

d = {
    'usd': 1000,
    'eur': 200,
    'jpy': 300,
    'chf': 2000,
    'cad': 222,
    'nzd': 233,
}

wyniki = {}


def wycen(waluta, kwota):
    r = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/?format=json')
    kurs = r.json()['rates'][0]['mid']
    wyniki[waluta] = round(kurs * kwota, 2)
    return round(kurs * kwota, 2)



if __name__ == '__main__':
    lista_watkow = []

    for waluta, kwota in d.items():
        lista_watkow.append(threading.Thread(target=wycen, args=(waluta, kwota)))

    for t in lista_watkow:
        t.start()

    for t in lista_watkow:
        t.join()

    print(wyniki)
    print(round(sum(wyniki.values()), 2))
