import json
from random import *
import mysql.connector

leTypeBaseVariante = ["0X0000BA20", "0X0000BA21", "0X0000BA22", "0X0000BA23", "0X0000BA24", "0X0000BA25", "0X0000BA26",
                      "0X0000BA27", "0X0000BA28", "0X0000BA29", "0X0000BA2A", "0X0000BA2B", "0X0000BA2C", "0X0000BA2D",
                      "0X0000BA2E", "0X0000BA2F"]


idAutomate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def CreerCouplesAutomateType(idAutom, lesTypes):
    coupleAutomateType = []
    for x in range(0, len(idAutom)):
        coupleAutomateType.append((idAutom[x], lesTypes[x]))

    return (coupleAutomateType)


def convertirTypeBase161Base10(lesTypes):
    for y in lesTypes:
        y = int(y, 16)
    return lesTypes


def CollecteAleatoire():

    for x in range(0, 9):
        numeroUnite = 1
        numeroAutomate = 1
        numeroAutomate = numeroAutomate + 1
        convertirTypeBase161Base10(leTypeBaseVariante)
        typeAutomate = leTypeBaseVariante[x]
        TemperatureCuve = round(uniform(2.5, 4), 1)
        temp = round(uniform(3512, 4607), 0)
        PoidsLait = round(uniform(3512, 4607), 0)
        PoidsProduitFini = 0
        if x == 0:
            PoidsProduitFini = PoidsLait
        else:
            PoidsProduitFini = PoidsLait - temp

        MesurePH = round(uniform(6.8, 7.2), 1)
        MesureK = round(uniform(35, 47), 0)
        ConcentrationNaCL = round(uniform(1, 1.7), 1)
        NivBactSalmonelle = round(uniform(17, 37), 0)
        NivBactEColi = round(uniform(35, 49), 0)
        NivBactListeria = round(uniform(28, 54), 0)


# au préalable , démarrer les daemons coté serveur ; HTTP et  MYSQL
# ainsi que les paquets  mysql-connector-python
# https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html
def doInsert():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="aubonbeurre")


mycursor = mydb.cursor()
