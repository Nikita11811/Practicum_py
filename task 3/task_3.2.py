import json


with open("RomeoAndJuliet.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data2 = []
for act in data["acts"]:
    for scene in act["scenes"]:
        characters = []
        for action in scene["action"]:
            if action["character"] not in characters:
                characters.append(action["character"])
        data2.append(characters)

with open("data2.json", 'w') as f:
    f.write(json.dumps(data2, ensure_ascii=False, indent=4))







