import requests
import json
import time
import threading
import sys


def salones():
    with open('oferta.json', 'r') as theFile:
        data = theFile.read()
        return data


def aCSV(elJson):
    jsonP = json.loads(elJson)
    print(jsonP)


datos = salones()
aCSV(datos)
