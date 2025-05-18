import multiprocessing.pool
import time


def f1(n):
    # print(f'startuje {multiprocessing.current_process()}, czas {n}\n', end='')
    time.sleep(n)
    # print(f'konczy sie {multiprocessing.current_process()}, czas {n}\n', end='')
    return f'wynik {multiprocessing.current_process().name}'


if __name__ == '__main__':
    # tworzenie obiektu wątku
    with multiprocessing.pool.Pool(16) as pool:
        w = pool.apply(f1, (1,))
        print(w)
        result = pool.apply_async(f1, (3,))
        print(result)
        while not result.ready():
            print('Working...')
            time.sleep(1)
        print(result.get())
        
        lista_parametrow = [2] * 16
        w = pool.map(f1, lista_parametrow)
        print(w)