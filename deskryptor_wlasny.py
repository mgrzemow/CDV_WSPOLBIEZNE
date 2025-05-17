class MojDeskryptor:
    def __init__(self, atr_name=None):
        self._atr_name = atr_name

    def __get__(self, instance, owner):
        print(f'__get__({instance}, {owner})')
        return getattr(instance, self._atr_name)

    def __set__(self, instance, value):
        setattr(instance, self._atr_name, value)
        print(f'__set__({instance}, {value})')

    def __set_name__(self, owner, name):
        if self._atr_name is None:
            self._atr_name = '_' + name


class Czlowiek:
    # __slots__ = [
    #     '_imie',
    #     '_nazwisko',
    # ]

    imie_nazwisko = MojDeskryptor('_inny')

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


if __name__ == '__main__':
    ...
    # c1 = Czlowiek('Adam Nowak')
    # print(c1.imie_nazwisko)
    # c1.imie_nazwisko = 'Ala Kowalska'
    # print(c1.imie_nazwisko)
