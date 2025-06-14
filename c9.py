import typing


class MultiMethod:

    def __init__(self, is_bound=False):
        self._d = {}
        self._is_bound = is_bound

    def register(self, f):
        th = typing.get_type_hints(f)
        if 'return' in th:
            del (th['return'])
        type_t = tuple(th.values())
        self._d[type_t] = f

    def __call__(self, *args, **kwargs):
        type_t = tuple(type(p) for p in args)
        if self._is_bound:
            type_t = type_t[1:]

        self._d[type_t](*args, **kwargs)


class mm_decorator:
    _d = {}

    def __init__(self, is_bound=False):
        self._is_bound = is_bound

    def __call__(self, f):
        name = f.__qualname__
        if name not in self.__class__._d:
            self.__class__._d[name] = MultiMethod(is_bound=self._is_bound)
        mm = self.__class__._d[name]
        mm.register(f)

        def f_nowa(*args, **kwargs):
            return mm(*args, **kwargs)

        return f_nowa


# int int
@mm_decorator()
def f1(x: int, y: int) -> int:
    print('int, int', type(x), type(y))
    return 77


# int str
@mm_decorator()
def f1(x: int, y: str) -> int:
    print('int, str', type(x), type(y))
    return 77


f1(1, 1)
f1(1, 'mama')


class A:
    # int int
    @mm_decorator(is_bound=True)
    def m1(self, x: int, y: int) -> int:
        print('int, int', type(x), type(y))
        return 77

    # int str
    @mm_decorator(is_bound=True)
    def m1(self, x: int, y: str) -> int:
        print('int, str', type(x), type(y))
        return 77


a = A()
a.m1(1, 1)
a.m1(1, 'mama')
