from xml.etree import ElementTree as ET


data = [
    {'x': 1, 'y': 10, 'z': 100},
    {'x': 2, 'y': 20, 'z': 200},
    {'x': 3, 'y': 30, 'z': 300},
    {'x': 4, 'y': 40, 'z': 400},
    {'x': 5, 'y': 50, 'z': 500}
]

root = ET.Element('records')

for item in data:
    record = ET.SubElement(root, 'record')
    for key, value in item.items():
        e = ET.SubElement(record, key)
        e.text = str(value)

tree = ET.ElementTree(root)
tree.write('data/output.xml', encoding='utf-8')