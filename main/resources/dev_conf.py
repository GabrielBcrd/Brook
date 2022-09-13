import configparser

# créer un objet configparser
config = configparser.ConfigParser()
# définir les sections et les clé/valeur

pathBdd = "E:\Brook\BDD"

config["InstrumentPath"]={
    "rim" : pathBdd + "\_Rim"
}

config["BddPath"]={
    "Langage" : "Python",
    "Langue" : "anglais"
}

# Enregistrer le fichier de configuration
with open("dev.application.conf", 'w') as f:
    config.write(f)
