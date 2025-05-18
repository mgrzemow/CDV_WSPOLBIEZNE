import multiprocessing.pool
import random
import time


def f1(d):
    id = d['task_id']
    czas = d['czas']
    time.sleep(czas)
    if random.randint(1, 100) < 20:
        raise ValueError(f'[{id}]Coś poszło nie tak.')

    return f'[{id}] wynik {multiprocessing.current_process().name}'



class MojCallback:
    def __init__(self, nazwa, ilosc):
        self.ilosc = ilosc
        self.nazwa = nazwa
        self.ile_gotowe = 0
        self.ile_bledow = 0
        self.wyniki = []

    def gotowe(self):
        return self.ile_gotowe + self.ile_bledow == self.ilosc

    def __repr__(self):
        return f'{self.nazwa}, gotowe: {self.ile_gotowe}, bledow: {self.ile_bledow} / {self.ilosc}'

    def __call__(self, wynik_lub_blad):
        if isinstance(wynik_lub_blad, BaseException):
            self.ile_bledow += 1
        else:
            self.ile_gotowe += 1
        self.wyniki.append(wynik_lub_blad)


if __name__ == '__main__':
    with multiprocessing.pool.Pool(16) as pool:

        lista_parametrow = [{'task_id':i, 'czas': 2} for i in range(60)]
        cb = MojCallback('Moja lista zadań', len(lista_parametrow))
        lista_taskow = [pool.apply_async(f1, (i,), callback=cb, error_callback=cb) for i in lista_parametrow]
        while not cb.gotowe():
            print(cb)
            time.sleep(1)

        print(cb.wyniki)
        wyniki = []
        for task in lista_taskow:
            try:
                wynik = task.get()
            except BaseException as e:
                wynik = e
            wyniki.append(wynik)
        print(wyniki)
        