import xml.etree.ElementTree as etree


tree = etree.parse("annot.opcorpora.no_ambig.xml")
root = tree.getroot()
l1 = []
l2 = []
l3 = []

for word in root.findall("text/paragraphs/paragraph/sentence/tokens/token"):
    for g in word.iter('g'):
        if g.attrib['v'] == "NOUN":
            l1.append(word.attrib['text'])
        elif g.attrib['v'] == "plur":
            l2.append(word.attrib['text'])
with open('xml2.txt', 'w', encoding="utf-8") as f:
    for word in l1:
        if word in l2:
            l3.append(word)
    f.write(str(l3))
