from c4 import wycen
import pytest
import requests

# 3785.3

class MojResponce:
    def json(self, *args, **kwargs):
        print('\nmonkeypatch json')
        return {"table":"A","currency":"dolar amerykański","code":"USD","rates":[{"no":"094/A/NBP/2025","effectiveDate":"2025-05-16","mid":3.7853}]}

def moje_get(*args, **kwargs):
    print('\nmonkeypatch get')
    return MojResponce()


def testuj_wycene(monkeypatch):
    with monkeypatch.context() as c:
        monkeypatch.setattr(requests, "get", moje_get)
        assert wycen('usd', 1000) == 3785.3
