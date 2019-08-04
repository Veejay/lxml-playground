import lxml
from lxml import etree
from io import StringIO

# read the contents of the HTML sample
file = open("./sample.html", "r")
markup = file.read()

# get a HTML parser instance ready
parser = etree.HTMLParser()

# parse the markup into an ElementTree
tree = etree.parse(StringIO(markup), parser)
print(tree)

# get the root of the tree 
# (in this case, a <html> tag that the parse method will automatically include for us)
root = tree.getroot()

# find all <p> tags in the document using XPath
paragraphs = root.findall('.//p')

# for each paragraph in the document, add a data-attribute
for paragraph in paragraphs:
    paragraph.set("data-foo", "kaboom")

# write the tree back to a file
tree.write("result.html")