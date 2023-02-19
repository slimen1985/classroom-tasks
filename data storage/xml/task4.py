from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()
children = list(root)

for child in children:
    print('{} {} {}'.format(
        child.find('./first_name').text,
        child.find('./last_name').text,
        child.find('./age').text,

    ))

# выборка всех тегов с заданным именем
first_name = root.findall('./person/first_name')
last_name = root.findall('./person/last_name')
age = root.findall('./person/age')


# Создаем словари из кортежей
for values in zip(first_name, last_name, age):
    row = {value.tag: value.text for value in values}
    print(row)