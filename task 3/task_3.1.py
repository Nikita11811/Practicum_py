import json

with open("data1.json", "a+", encoding="utf-8") as f:
    for line in open("wikidata_1000.json", 'r', encoding="utf-8"):
        data = json.loads(line)
        try:
            json.dump({data["label"]["value"]: data["description"]["value"]}, f, sort_keys=True, indent=4)
        except KeyError:
            json.dump({data["label"]["value"]: None}, f, sort_keys=True, indent=4)


