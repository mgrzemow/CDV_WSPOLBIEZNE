def auto_slots(cls_name, cls_inh, cls_dict):
    slots = cls_dict.get('__slots__', [])
    for atr_name, atr_value in cls_dict.items():
        if isinstance(atr_value, property):
            slots.append(f'_{atr_name}')
        # jeżeli atr_val jest instancją property to dodaj opdowiednią nazwę do __slots__
    cls_dict['__slots__'] = slots
    return type(cls_name, cls_inh, cls_dict)

class A(metaclass=auto_slots):
    def _get_atr1(self):
        return self._atr1

    def _set_atr1(self, value):
        self._atr1 = value

    atr1 = property(fget=_get_atr1, fset=_set_atr1)

    def __init__(self, atr1):
        self.atr1 = atr1

a = A(123)
print(a.atr1)
a.atr2 = 'asdasd'
