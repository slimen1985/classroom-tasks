from xml.etree import ElementTree as ET

root = ET.Element('record')
for i in range(10):
    sub_element = ET.SubElement(root, 'value{}'.format(i))
    sub_element.text = str(i * 10)

ET.dump(root)

