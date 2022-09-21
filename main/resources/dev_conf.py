import configparser

# créer un objet configparser
config = configparser.ConfigParser()
# définir les sections et les clé/valeur

pathBdd = "E:\Brook\BDD"
pathBddSample = "\Sample"

config["InstrumentPath"]={
    "rim" : pathBdd + pathBddSample + "\_Rim",
    "closedHiHat" : pathBdd + pathBddSample + "\_HiHatClosed"
}

# Enregistrer le fichier de configuration
with open("dev.application.conf", 'w') as f:
    config.write(f)
