import collections
import json


with open("RomeoAndJuliet.json", "r", encoding="utf-8") as f:
    data = json.load(f)

a = collections.defaultdict(list)
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                a[action["character"]].append(line)

with open('task5_2.json', 'w') as f:
    json.dump(a, f, ensure_ascii=False, indent=4)