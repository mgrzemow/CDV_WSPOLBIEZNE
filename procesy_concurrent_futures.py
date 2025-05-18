import concurrent.futures as futures
import multiprocessing
import random
import time


def f1(d):
    id = d['task_id']
    czas = d['czas']
    time.sleep(czas)
    if random.randint(1, 100) < 20:
        raise ValueError(f'[{id}]Coś poszło nie tak.')

    return f'[{id}] wynik {multiprocessing.current_process().name}'

if __name__ == '__main__':
    with futures.ProcessPoolExecutor(16) as executor:

        lista_parametrow = [{'task_id': i, 'czas': 2} for i in range(60)]
        # wywali się lokalnie z wyjątkiem przechwyconym w podprocesie

        # for wynik in executor.map(f1, lista_parametrow):
        #     print(wynik)

        lista_taskow = [executor.submit(f1, p) for p in lista_parametrow]
        for future in futures.as_completed(lista_taskow):
            e = future.exception()
            if e is None:
                print(future.result())
            else:
                print(e)
        

