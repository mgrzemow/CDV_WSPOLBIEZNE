class Czlowiek:
    __slots__ = [
        '_imie',
        '_nazwisko',
    ]

    def _set_imie_nazwisko(self, imie_nazwisko):
        print(f'setter {imie_nazwisko}')
        imie, nazwisko = imie_nazwisko.split()
        self._imie = imie
        self._nazwisko = nazwisko

    def _get_imie_nazwisko(self):
        print('getter')
        return f'{self._imie} {self._nazwisko}'

    imie_nazwisko = property(fset=_set_imie_nazwisko,
                             fget=_get_imie_nazwisko)

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


class Czlowiek:
    __slots__ = [
        '_imie',
        '_nazwisko',
    ]

    @property
    def imie_nazwisko(self):
        print('getter')
        return f'{self._imie} {self._nazwisko}'

    @imie_nazwisko.setter
    def imie_nazwisko(self, imie_nazwisko):
        print(f'setter {imie_nazwisko}')
        imie, nazwisko = imie_nazwisko.split()
        self._imie = imie
        self._nazwisko = nazwisko

    def __init__(self, imie_nazwisko):
        self.imie_nazwisko = imie_nazwisko


if __name__ == '__main__':
    c1 = Czlowiek('Adam Nowak')
    print(c1.imie_nazwisko)
    c1.imie_nazwisko = 'Ala Kowalska'
    print(c1.imie_nazwisko)
