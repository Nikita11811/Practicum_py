import json

with open('wikidata_1000.json', 'r', encoding='utf-8') as f:
    dic = {}
    for row in f:
        line = json.loads(row)
        word = line["label"]["value"]
        try:
            dic[word] = line["description"]["value"]
        except KeyError:
            dic[word] = 'None'

with open("data1.json", "w", encoding='utf-8') as g:
    json.dump(dic, g, sort_keys=False, indent=4, ensure_ascii=False)
