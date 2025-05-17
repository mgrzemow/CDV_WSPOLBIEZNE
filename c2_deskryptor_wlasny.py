import collections


class MojDeskryptor:
    def __init__(self, atr_name=None):
        self._atr_name = atr_name
        self._history = collections.defaultdict(list)

    def __get__(self, instance, owner):
        if instance is not None:
            return getattr(instance, self._atr_name)
        else:
            return self

    def __set__(self, instance, value):
        self._history[id(instance)].append(value)
        print(self._history)
        setattr(instance, self._atr_name, value)

    def __set_name__(self, owner, name):
        if self._atr_name is None:
            self._atr_name = '_' + name

    def get_history(self, instance):
        return self._history[id(instance)]

class Czlowiek:
    # __slots__ = [
    #     '_imie',
    #     '_nazwisko',
    # ]

    imie_nazwisko = MojDeskryptor()

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


# dopisać pamiętanie historii wartości atrybutu
# za każdym zapisem niech się wypisuje historia - prosta lista

# uwaga - co będzie jeżeli będą 2 instancje klasy Czlowiek?

if __name__ == '__main__':
    c1 = Czlowiek('Adam Nowak')
    print(c1.imie_nazwisko)
    c1.imie_nazwisko = 'Ala Kowalska'
    print(c1.imie_nazwisko)
    print(c1)
    c2 = Czlowiek('Ewa Nowak')
    print(c2.imie_nazwisko)
    c2.imie_nazwisko = 'Ola Kowalska'
    print(c2.imie_nazwisko)

    print(c2.__class__.imie_nazwisko._history)
    print(c2.__class__.imie_nazwisko.get_history(c2))
    print(Czlowiek.imie_nazwisko.get_history(c2))
    