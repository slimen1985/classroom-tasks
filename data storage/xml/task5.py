from lxml import etree as ET

root = ET.parse('data/test_ns.xml')

# for i in root.findall('{http://example.com/persons}person'):
#     name = i.find('{http://example.com/persons}name').text
#     nik_name = i.find('{http://example.com/olympic}name').text
#     field = i.find('{http://example.com/olympic}field').text
#
#     print('{} {} -> {}'.format(name, nik_name, field))


ns = {
    'persons': "http://example.com/persons",
    'olympic': "http://example.com/olympic"
}

for i in root.findall('persons:person', ns):
    name = i.find('persons:name', ns).text
    nik_name = i.find('olympic:name', ns).text
    field = i.find('olympic:field', ns).text

    print('{} {} -> {}'.format(name, nik_name, field))