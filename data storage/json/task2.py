import json

data = '{"fname":"Vadim", "lname":"Liubin", "age": 37, "hobbies": ["writer","poetry","books"]}'

data_ = json.loads(data)
print(type(data_))
print(type(data))


with open('data/output.json', "r") as file:
    json_data = json.load(file)
    print(json_data)