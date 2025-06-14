class SingletonKlasa:
    """
    Prosta implementacja na klasie - problemy z wielodziedziczeniem.
    """
    def __repr__(self):
        return f'{self.__class__.__name__}({id(self)})'

    _d = {}

    def __new__(cls, *args, **kwargs):
        ...
        # za pierwszym razem stworzyć instancję i zapisać jako atrybut klasowy
        # za kolejnymi - zwrócić
        if cls not in cls._d:
            cls._d[cls] = super().__new__(cls, *args, **kwargs)
        return cls._d[cls]


class MojaKlasa(SingletonKlasa):
    """
    To jest klasa która ma mieć cechy singletona.
    """
    ...


class SingletonMaster:
    @classmethod
    def get_singleton(cls):
        if not hasattr(cls, '_singleton'):
            cls._singleton = SingletonKlasa()
        return cls._singleton


# implementacja singletona - najpewniejsza - metaklasa:
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MojaKlasa(metaclass=Singleton):
    ...

class MojaKlasa1(MojaKlasa):
    ...

if __name__ == '__main__':
    s4 = MojaKlasa()
    print(s4)
    s5 = MojaKlasa()
    print(s5)
    s6 = MojaKlasa()
    print(s6)

    s7 = MojaKlasa1()
    print(s7)
    s8 = MojaKlasa1()
    print(s8)
    s9 = MojaKlasa1()
    print(s9)
