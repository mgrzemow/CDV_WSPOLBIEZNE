import json
import os
from pprint import pprint
from zipfile import ZipFile

import pytest
from c7_do_testow import podziel, dodaj_i_zaokraglij

dane_testowe = [
    [[45, 67], 0.6716417910447762],
    [[84, 25], 3.36],
    [[22, 21], 1.0476190476190477],
    [[81, 45], 1.8],
    [[74, 67], 1.1044776119402986],
    [[52, 6], 8.666666666666666],
    [[25, 13], 1.9230769230769231],
    [[8, 83], 0.0963855421686747],
    [[88, 4], 22.0],
    [[100, 83], 1.2048192771084338]
]


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


@pytest.mark.parametrize('args, w', dane_testowe)
def test_parametrize(args, w):
    assert pytest.approx(w) == podziel(*args)

# @pytest.fixture(scope='module')
# def dane_testowe_fixture():
#     # to zwraca globalną listę ale w praktyce - wczytuje z pliku, bazy itd
#     print('\ndane_testowe_fixture start')
#     yield dane_testowe
#     print('\ndane_testowe_fixture koniec')
#
# def test_uzycie_fixture_1(dane_testowe_fixture):
#     for args, w in dane_testowe_fixture:
#         assert pytest.approx(w) == podziel(*args)
#
# def test_uzycie_fixture_2(dane_testowe_fixture):
#     for args, w in dane_testowe_fixture:
#         assert pytest.approx(w) == podziel(*args)

# wyrzucić dane testowe do pliku json spakjowanego zipem
# napisać fixture, który najpierw wypakuje plik, wczyta dane z jsona, a po użyciu skasuje wypakowany plik

@pytest.fixture(scope='module')
def dane_testowe_fixture_z_pliku():
    with ZipFile('dane_testowe.zip') as zip:
        zip.extractall()

    with open('dane_testowe.json', 'rt') as f:
        dane = json.load(f)
    print('\ndane_testowe_fixture_z_pliku start')
    yield dane
    os.remove('dane_testowe.json')
    print('\ndane_testowe_fixture_z_pliku koniec')

def test_uzycie_fixture_3(dane_testowe_fixture_z_pliku):
    for args, w in dane_testowe_fixture_z_pliku:
        assert pytest.approx(w) == podziel(*args)

def test_uzycie_fixture_4(dane_testowe_fixture_z_pliku):
    for args, w in dane_testowe_fixture_z_pliku:
        assert pytest.approx(w) == podziel(*args)