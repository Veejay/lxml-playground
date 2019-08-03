import lxml
from lxml import etree
from io import StringIO

markup = '''
    <html>
        <head>
        </head>
        <body>
            <p class="acme">
                Hello!
            </p>
        </body>
    </html>
'''

parser = etree.HTMLParser()
tree = etree.parse(StringIO(markup), parser)
paragraph = tree.find(".//p")
print(paragraph.attrib["class"])
