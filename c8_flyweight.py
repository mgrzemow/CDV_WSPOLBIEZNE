class FlyweightPoint:
    """
    Prosta implementacja na klasie - problemy z wielodziedziczeniem.
    """
    _instances = {}

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x=}, {self.y=}, id={id(self)})'

    def __new__(cls, x, y):
        ...
        # za pierwszym razem stworzyć instancję i zapisać jako atrybut klasowy
        # za kolejnymi - zwrócić
        if (x, y) not in cls._instances:
            cls._instances[(x, y)] = super().__new__(cls)
        return cls._instances[(x, y)]

    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    p1 = FlyweightPoint(1, 2)
    print(p1)
    p2 = FlyweightPoint(1, 8)
    print(p2)
    p3 = FlyweightPoint(1, 8)
    print(p3)
    p4 = FlyweightPoint(1, 8)
    print(p4)
    p5 = FlyweightPoint(2, 8)
    print(p5)
    # przerobić singletona tak żeby istniała tylko jedna instancja dla
    # puntów o tych samych kordynatach
