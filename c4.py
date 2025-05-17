# mając dany portfel walutowy:
d = {
    'usd': 1000,
    'eur': 200,
    'jpy': 300,
    'chf': 2000
}

# policzyć jego wartość w złotówkach za pomocą tylu watków ile walut
# w każdym z wątków wysłać zapytnie do API NBP:
# https://api.nbp.pl/api/exchangerates/rates/a/chf/?format=json
# paczka requests
import requests
r = requests.get('https://api.nbp.pl/api/exchangerates/rates/a/chf/?format=json')
kurs = r.json()['rates'][0]['mid']
print(kurs)
# zapis do globalnego słownika
wyniki = {}
# wyliczyć wartość koszyka w PLN