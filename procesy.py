import multiprocessing
import time


def f1(n):
    print(f'startuje {multiprocessing.current_process()}, czas {n}\n', end='')
    time.sleep(n)
    print(f'konczy sie {multiprocessing.current_process()}, czas {n}\n', end='')
    d[multiprocessing.current_process()] = 'wynik'

d = {}

if __name__ == '__main__':
    # tworzenie obiektu wątku
    t1 =  multiprocessing.Process(target=f1, args=(5,), daemon=False)
    t2 =  multiprocessing.Process(target=f1, args=(5,), daemon=False)
    t3 =  multiprocessing.Process(target=f1, args=(5,), daemon=False)

    # uruchomienie wątku
    t1.start()
    t2.start()
    t3.start()

    # czekamy na zakończenie wątku
    t1.join()
    t2.join()
    t3.join()

    print(d)