import json
from unidecode import unidecode

# Ouvrir le fichier JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Enlever les accents de chaque chaîne de caractères dans le fichier JSON
for intent in data["intents"]:
    intent["tag"] = unidecode(intent["tag"])
    pattern_list = []
    for pattern in intent["patterns"]:
        pattern_list.append(unidecode(pattern))
    intent["patterns"]=pattern_list

# Écrire les modifications dans le fichier JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
