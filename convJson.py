import requests
import json
import time
import threading
import sys
from collections import OrderedDict

def salones():
    with open('oferta.json', 'r') as theFile:
        data = theFile.read()
        return data


def aCSV(elJson):
    salones=[]
    jsonP = json.loads(elJson)
    for x in jsonP['records']:
        sal = x['salon'].split(";;")
        for b in sal:
            b = b.replace(".", "")
            salones.append(b)
    salones = list(OrderedDict.fromkeys(salones))
    salones = sorted(salones)
    with open('salones.txt', 'w') as theFile:
        for x in salones:
            theFile.write(str(x)+"\n")


datos = salones()
aCSV(datos)
