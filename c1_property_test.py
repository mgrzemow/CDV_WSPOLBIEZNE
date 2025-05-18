"""
przetestować klasę Host
1. Walidacja ilosci sekcji - czy wylatuje błąd #
2. Walidacja liczb z przedziału- czy wylatuje błąd #
3. Walidacja że są liczbami- czy wylatuje błąd #
4. Czy jest atrybut .ip_tuple #
5. Czy działa poprawny numer ip #
6. Że ip_tuple jest read_only #
7. Czy obiekt się zachowuje poprawnie, czy jest __slots__ #
"""
import pytest

from c1_property import Host


def test_podstawowe():
    h1 = Host('1.2.3.4')
    h2 = Host('5.6.7.8')
    assert h1.ip == '1.2.3.4'
    assert h2.ip == '5.6.7.8'
    h1.ip = '1.2.3.99'
    h2.ip = '5.6.7.10'
    assert h1.ip == '1.2.3.99'
    assert h2.ip == '5.6.7.10'


def test_graniczne():
    h1 = Host('0.0.0.0')
    assert h1.ip == '0.0.0.0'
    h1.ip = '255.255.255.255'
    assert h1.ip == '255.255.255.255'
    h1 = Host('1.1.1.1')
    assert h1.ip == '1.1.1.1'
    h1.ip = '254.254.254.254'
    assert h1.ip == '254.254.254.254'


def test_slots():
    h1 = Host('1.2.3.4')
    with pytest.raises(AttributeError):
        h1.jakis_atr = 123


def test_ip_tuple():
    h1 = Host('1.2.3.4')
    assert h1.ip_tuple == (1, 2, 3, 4)
    with pytest.raises(AttributeError, match='has no setter'):
        h1.ip_tuple = 12
    Host('1.2..3.4')


def test_validacja_ilosc_sekcji():
    with pytest.raises(ValueError, match=r'ip address must have 4 number'):
        h1 = Host('1.2.3')
    with pytest.raises(ValueError, match=r'ip address must have 4 number'):
        h1 = Host('1.2.3.2.3')
    with pytest.raises(ValueError, match=r'ip address must have 4 number'):
        h1 = Host('.'.join(['1.2.3.2.3'] * 100))
    with pytest.raises(ValueError, match=r'ip address must have 4 number'):
        h1 = Host('')

    with pytest.raises(ValueError, match=r'ip address must have 4 number'):
        h1 = Host('1.2.3.4')
        h1.ip = '1.2.3'
    with pytest.raises(ValueError, match=r'ip address must have 4 number'):
        h1 = Host('1.2.3.4')
        h1.ip = '1.2.3.2.3'
    with pytest.raises(ValueError, match=r'ip address must have 4 number'):
        h1 = Host('1.2.3.4')
        h1.ip = '.'.join(['1.2.3.2.3'] * 100)
    with pytest.raises(ValueError, match=r'ip address must have 4 number'):
        h1 = Host('1.2.3.4')
        h1.ip = ''


def west_walidacja_wartosci():
    with pytest.raises(ValueError, match=r'ip address must be in range'):
        h1 = Host('256.2.3.4')
    with pytest.raises(ValueError, match=r'ip address must be in range'):
        h1 = Host('-1.2.3.4')
    with pytest.raises(ValueError, match=r'ip address must be in range'):
        h1 = Host('-213123211.2.3.4')
    with pytest.raises(ValueError, match=r'ip address must be in range'):
        h1 = Host('342344213123211.2.3.4')


def west_walidacja_wartosci():
    with pytest.raises(ValueError):
        h1 = Host('256.2.3.asdasd')


def test_dziwne():
    h1 = Host('1.2.3..4')
    assert h1.ip == '1.2.3.4'
