def moja_pierwsza_meta(cls_name, cls_inh, cls_dict):
    return type(cls_name, cls_inh, cls_dict)

class A(metaclass=moja_pierwsza_meta):
    ...

# np wstrzykujemy do słownika klasowego
def moja_pierwsza_meta(cls_name, cls_inh, cls_dict):
    cls_dict['version'] = '1.2.3'
    return type(cls_name, cls_inh, cls_dict)

class A(metaclass=moja_pierwsza_meta):
    ...

print(A.version)

