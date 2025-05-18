class Host:
    __slots__ = ['_ip']

    def _set_ip(self, ip):
        w = tuple(int(i) for i in ip.split('.') if i)
        if len(w) != 4:
            raise ValueError(f'ip address must have 4 number, got: {ip}')
        if not all(0 <= i <= 255 for i in w):
            raise ValueError(f'ip address must be in range 0-255, got: {ip}')
        self._ip = w

    def _get_ip(self):
        return '.'.join(str(i) for i in self._ip)

    ip = property(fset=_set_ip, fget=_get_ip)

    @property
    def ip_tuple(self):
        return self._ip
    

    def __init__(self, ip):
        self.ip = ip

if __name__ == '__main__':
    h1 = Host('192.168.127.12')
    print(h1.ip)
    h1.ip = '8.8.8.8'
    print(h1.ip)
    print(h1.ip_tuple)
    
    # zamienić ip na property
    # tak aby przechowywać nr ip w krotce (192,168,0,1)
    # walidacja - poniższe operacje mają się wywalić z błędem ValueError
    # 4 człony numeru
    # h1.ip = '8.8.8'
    # h1.ip = '8.8.8.8.8'
    # każdy z członów - z przedziału 0..255
    # h1.ip = '192.168.0.ala'
    # h1.ip = '192.168.0.999'