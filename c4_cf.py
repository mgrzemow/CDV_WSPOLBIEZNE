# mając dany portfel walutowy:
import random
import threading
import time

import requests
import concurrent.futures as cf

# policzyć jego wartość w złotówkach za pomocą tylu watków ile walut
# w każdym z wątków wysłać zapytnie do API NBP:
# https://api.nbp.pl/api/exchangerates/rates/a/chf/?format=json
waluty = ['THB', 'USD', 'AUD', 'HKD', 'CAD', 'NZD', 'SGD', 'EUR', 'HUF', 'CHF', 'GBP', 'UAH', 'JPY', 'CZK', 'DKK', 'ISK', 'NOK', 'SEK', 'RON', 'BGN', 'TRY', 'ILS', 'CLP', 'PHP', 'MXN', 'ZAR', 'BRL', 'MYR', 'IDR', 'INR', 'KRW', 'CNY', 'XDR']
d = {w: random.randint(1000, 5000) for w in waluty}

def wycen(krotka):
    waluta, kwota = krotka
    r = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/?format=json')
    kurs = r.json()['rates'][0]['mid']
    return round(kurs * kwota, 2)


# użyć concurrent futures zamiast watków
# ThreadPoolExecutor

if __name__ == '__main__':
    for n in [1, 2, 4, 8, 16, 32]:
        with cf.ThreadPoolExecutor(n) as ex:
            t1 = time.perf_counter()
            suma = 0
            for w in ex.map(wycen, d.items()):
                suma = round(suma + w, 2)

            # suma = round(sum(w for w in ex.map(wycen, d.items())), 2)
            print(f'{n} watkow, czas {time.perf_counter() - t1:.2f} s. wynik: {suma}')
