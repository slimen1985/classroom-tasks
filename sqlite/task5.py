import xml.etree.ElementTree as ET
import json

# root = ET.Element('data')
# items = ET.SubElement(root, 'items')
#
# for i in range(1, 5):
#     item = ET.SubElement(items, 'item', attrib={"name": f"item{i}"})
#     item.text = str(i * 10)
#
# tree = ET.ElementTree(root)
# tree.write('data.xml')

tree = ET.parse('data.xml')

root = tree.getroot()
items = root[0]
res = []

for item in items:
    res.append({item.attrib.get('name'): item.text})

print(res)
print(json.dumps(res))