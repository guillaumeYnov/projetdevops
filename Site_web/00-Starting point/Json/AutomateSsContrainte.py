import json

data_set = {"NumeroUnité": [],
            "NuméroAutomate":[],
            "TypeAutomate" : [],
            "Temperaturecuve" : [],
            "TemperatureExterieur" : [],
            "Poidsdulaitencuve" : [],
            "PoidsDuProduitFini" : [],
            "MesurePH" : [],
            "MesureK+" : [],
            "concentrationNaCL" : [],
            "niveauBacterienSalmonelle" : [],
            "niveauBacterienEColi" : [],
            "niveauBacterienListeria" : [],}

#création structure
json_dump = json.dumps(data_set)
# insert contenu
json_object = json.loads(json_dump)


print(json_object["NumeroUnité"])

