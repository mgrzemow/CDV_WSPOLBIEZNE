class A:
    atr1 = 'mama'
    def m1(self):
        print('A.m1')

def m1(self):
    print('klasa_zrobiona_z_type.m1')

cls_dict = {
    'atr1': 'mama',
    'm1': m1
}

# parametry: nazwa, krotka dziedziczenia, slownik klasowy
New_A = type('A', (), cls_dict)
print(New_A)
o = New_A()
o.m1()
print(o.atr1)
