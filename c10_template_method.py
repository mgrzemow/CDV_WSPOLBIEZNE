import abc


class AbstractPizzaMaker(metaclass=abc.ABCMeta):
    def make_pizza(self):
        self.make_dough()
        self.add_toppings()
        self.add_cheese()

    @abc.abstractmethod
    def make_dough(self):
        ...

    @abc.abstractmethod
    def add_toppings(self):
        print('Adding sause..')

    @abc.abstractmethod
    def add_cheese(self):
        ...


class PizzaMaker(AbstractPizzaMaker):
    def make_dough(self):
        print('Making dough')

    def add_toppings(self):
        super().add_toppings()
        print('Adding toppings')

    def add_cheese(self):
        print('Adding cheese')


pm = PizzaMaker()
pm.make_pizza()
