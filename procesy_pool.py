import multiprocessing.pool
import random
import time


def f1(n):
    # print(f'startuje {multiprocessing.current_process()}, czas {n}\n', end='')
    time.sleep(n)
    # print(f'konczy sie {multiprocessing.current_process()}, czas {n}\n', end='')
    if random.randint(1,100) > 20:
        raise ValueError('Coś poszło nie tak.')
    
    return f'wynik {multiprocessing.current_process().name}'


def f_callback(wynik):
    print(f'callback dostał {wynik}')


class MojCallback:
    def __init__(self, nazwa, ilosc):
        self.ilosc = ilosc
        self.nazwa = nazwa

    def gotowe(self):
        ...

    def __repr__(self):
        ...

    def __call__(self, wynik_lub_blad):
        print(f'callback dostał {wynik_lub_blad}')


if __name__ == '__main__':
    # tworzenie obiektu wątku
    with multiprocessing.pool.Pool(16) as pool:
        # w = pool.apply(f1, (1,))
        # print(w)
        # result = pool.apply_async(f1, (3,))
        # print(result)
        # while not result.ready():
        #     print('Working...')
        #     time.sleep(1)
        # print(result.get())
        #
        # lista_parametrow = [2] * 16
        # w = pool.map(f1, lista_parametrow)
        # print(w)
        #
        # lista_parametrow = [(2,)] * 16
        # w = pool.starmap(f1, lista_parametrow)
        # print(w)
        #
        # lista_parametrow = [2] * 16
        # result = pool.map_async(f1, lista_parametrow)
        # print(result)
        # while not result.ready():
        #     print('Working...')
        #     time.sleep(1)
        # print(result.get())

        lista_parametrow = [2] * 160
        cb = MojCallback('Moja lista zadań', len(lista_parametrow))
        lista_taskow = [pool.apply_async(f1, (i,), callback=cb, error_callback=cb) for i in lista_parametrow]
        while not cb.gotowe():
            print(cb)
            time.sleep(1)

        print(cb.wyniki)
