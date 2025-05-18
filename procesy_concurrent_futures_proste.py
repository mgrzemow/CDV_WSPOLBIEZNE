import concurrent.futures as futures
import multiprocessing
import random
import time


def f1(d):
    id = d['task_id']
    czas = d['czas']
    time.sleep(czas)
    return f'[{id}] wynik {multiprocessing.current_process().name}'


if __name__ == '__main__':
    with futures.ProcessPoolExecutor(16) as executor:

        lista_parametrow = [{'task_id': i, 'czas': 2} for i in range(60)]
        # wywali się lokalnie z wyjątkiem przechwyconym w podprocesie

        for wynik in executor.map(f1, lista_parametrow):
            print(wynik)
