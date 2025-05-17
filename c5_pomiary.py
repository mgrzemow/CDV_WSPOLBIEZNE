# napisać 3 funkcje:
import threading
import timeit
import requests
import multiprocessing


def dos(n):
    # wysyła n requestów na adres: http://gatling.io
    s = requests.Session()
    for _ in range(n):
        r = s.get('http://gatling.io')


def fibo(n):
    # wylicza nty wyraz ciągu fibonnaciego 1 1 2 3 5 8 13 21
    # uwaga - nie rekurencyjnie
    x1 = x2 = 1
    for _ in range(n):
        x1, x2 = x2, x1 + x2
    return x2


def n_times_fibo(m):
    # wylicza m razy wyraz ciagu o nr 10_000
    for _ in range(m):
        r = fibo(10_000)


# wp - watek lub process
def run_parallell(funkcja, ile_zadan, ile_wp, klasa):
    zadan_na_wp = ile_zadan // ile_wp
    lista_wp = [klasa(target=funkcja, args=(zadan_na_wp,))
                for _ in range(ile_wp)]
    [wp.start() for wp in lista_wp]
    [wp.join() for wp in lista_wp]


if __name__ == '__main__':
    for i in [16, 32, 64, 128]:
        t = timeit.timeit(f'run_parallell(dos, 10000, {i}, threading.Thread)',
                          number=1,
                          globals=globals())
        print(f'{i}: {t}')
