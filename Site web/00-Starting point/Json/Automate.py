import json
import jsonschema
from jsonschema import validate

Automate = {

    "title": "Automate",
    "type": "object",
    "properties": {

            "numeroUnite": {
                "description": "Cle unite",
                "type": "integer"

            },
        "numéroAutomate": {
                "description": "Identifiant de l'automate",
                "type": "integer"
                },
        "typeAutomate": {
                "description": "Identifiant type",
                "type": "integer"
                },
        "temperatureCuve": {
                "description": "Température de la cuve",
                "type": "float"
                },

        "temperatureExterieure": {
                "description": "Temperature exterieure",
                "type": "float"
                },
        "poidsLait": {
                "description": "Poids lait supporté exprimé en kg",
                "type": "float"
                },

        "poidsProduit": {
                "description": "Poids du produit fini réalisé",
                "type": "float"
                },
        "mesurePh": {
                "description": "Mesure du PH",
                "type": "float"
                },
        "mesureK+": {
                "description": "Mesure du Potassium",
                "type": "integer"
                },
        "concentNacl": {
                "description": "Mesure de la concentration de sel",
                "type": "float"
                },
        "nivBactSalmo": {
                "description": "Mesure du niveau bactérien (salmonel)",
                "type": "integer"
                },
        "nivBactColi": {
                "description": "Mesure du niveau bactérien (E-Coli)",
                "type": "integer"
                },
        "nivBactList": {
                "description": "Mesure du niveau bactérien (Listéria)",
                "type": "integer"
                },
        # remplir les autres champs , fastidieux , pas le temps



    }
}


# stocke la strcuture dans un objet inetrmédiaire
json_dump = json.dumps(Automate)
