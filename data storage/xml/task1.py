from xml.etree import ElementTree as ET

# Создаем объект дерево и берем корневой тэг
tree = ET.parse('data/test.xml')
root = tree.getroot()

# Создаем список дочерних элементов
children = list(root)
print(children)


for child in children:
    # print("PK: ", child.attrib)
    for item in child:
        # Выводим тэги и их значения
        print("{}: {}".format(item.tag, item.text))

