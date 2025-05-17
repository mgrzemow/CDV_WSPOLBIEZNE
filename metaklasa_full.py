class Meta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print()
        print(f'  Meta.__prepare__({mcs=}, {name=}, {bases=}, {kwargs=})')
        return {'atr5': 99}

    # Most commonly - here!!!:
    def __new__(mcs, name, bases, attrs, **kwargs):
        print()
        print(f'  Meta.__new__({mcs=}, {name=}, {bases=}, {attrs=}, {kwargs=})')
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs, **kwargs):
        print()
        print(f'  Meta.__init__({cls=}, {name=}, {bases=}, {attrs=}, {kwargs=})')
        return super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print()
        print(f'  Meta.__call__({cls=}, {args=}, {kwargs=})')
        return super().__call__(*args, **kwargs)


class A(metaclass=Meta, suffix='_get', akuku=99):
    cls_atr1 = 9

    def m1(self, x, y):
        print('m1', x, y)

    def __new__(cls, *args, **kwargs):
        print()
        print(f'  Class.__new__({cls=}, {args=}, {kwargs=})')
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print()
        print(f'  Class.__init__({self=}, {args=}, {kwargs=})')


a = A('Jan', 'Nowak')
# # print(a.atr5)
