class A:
    def m1(self):
        print('A.m1')

class B:
    def m1(self):
        print('B.m1')

def rob_cos():
    return A()

d = {
    'raz': A,
    'dwa': B,
    'trzy': rob_cos
}

cos = d['dwa']

instancja = cos()
instancja.m1()
