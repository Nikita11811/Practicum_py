import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

characters = {}
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in characters:
                characters[action["character"]] = 1
            else:
                characters[action["character"]] += 1

max_rep = 0
name = ""
for character in characters:
    if characters[character] >= max_rep:
        max_rep = characters[character]
        name = character

print(name)
print(max_rep, "реплики")
