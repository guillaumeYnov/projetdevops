import json
import jsonschema
from jsonschema import validate

Automate = {
 
 	"title":"Automate",
 	"type":"object",
 	"properties":{

 		"numeroUnite":{
         "description":"cle unite",
         "type":"integer"

      },
      "numéroAutomate":{
         "description":"identifiant Automate",
         "type":"integer"
      },
      "typeAutomate":{
         "description":"identifiant type",
         "type":"integer"
      },
       "temperatureCuve":{
         "description":"temp cuve",
         "type":"float"
      },

      "temperatureExterieure":{
         "description":"temperatureExterieure",
         "type":"float"
      },
      "poidsLait":{
         "description":"poids laiit supporté exprimé en kg",
         "type":"float"
      }
      # remplir les autres champs , fastidieux , pas le temps



 	}
}




#stocke la strcuture dans un objet inetrmédiaire
json_dump = json.dumps(Automate)


