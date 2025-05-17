import threading
import time


def f1(n):
    print(f'startuje {threading.current_thread()}, czas {n}\n', end='')
    time.sleep(n)
    print(f'konczy sie {threading.current_thread()}, czas {n}\n', end='')
    d[threading.current_thread()] = 'wynik'

d = {}
# tworzenie obiektu wątku
t1 =  threading.Thread(target=f1, args=(5,), daemon=False)
t2 =  threading.Thread(target=f1, args=(5,), daemon=False)
t3 =  threading.Thread(target=f1, args=(5,), daemon=False)

# uruchomienie wątku
t1.start()
t2.start()
t3.start()

# czekamy na zakończenie wątku
t1.join()
t2.join()
t3.join()

print(d)