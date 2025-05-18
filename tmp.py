import json
import os
from pprint import pprint
from zipfile import ZipFile

with ZipFile('dane_testowe.zip') as zip:
    zip.extractall()

with open('dane_testowe.json', 'rt') as f:
    dane = json.load(f)
    pprint(dane)

os.remove('dane_testowe.json')