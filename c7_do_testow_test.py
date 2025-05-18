import pytest
from c7_do_testow import podziel, dodaj_i_zaokraglij


def test_podziel_calkowite():
    assert podziel(4, 2) == 2
    assert podziel(6, 2) == 3
    assert podziel(10, 2) == 5


def test_podziel_floaty():
    assert podziel(3.5, 2) == 1.75
    assert podziel(4.8, 1.6) == pytest.approx(3)
    assert podziel(10, 3) == pytest.approx(3.3333333333333333)

def test_podziel_bledy():
    with pytest.raises(ZeroDivisionError, match=r'division by zero'):
        podziel(4, 0)
    with pytest.raises(ZeroDivisionError, match=r'division by zero'):
        podziel(3, 0)


def test_dodaj_i_zaokraglij():
    assert dodaj_i_zaokraglij(.1, .2) == .3
