import xml.etree.ElementTree as etree


tree = etree.parse("annot.opcorpora.no_ambig.xml")
root = tree.getroot()

with open('xml1.txt', 'w', encoding="utf-8") as f:
    for tag in root.findall("text/paragraphs/paragraph/sentence/source"):
        f.write(tag.text)
        f.write("\n")





