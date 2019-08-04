import lxml
from lxml import etree
from io import StringIO


file = open("./sample.html", "r")
markup = file.read()

parser = etree.HTMLParser()
tree = etree.parse(StringIO(markup), parser)
print(tree)

root = tree.getroot()

paragraphs = root.findall('.//p')

for paragraph in paragraphs:
    paragraph.set("data-foo", "bang")

tree = etree.ElementTree(root)
tree.write("result.html")