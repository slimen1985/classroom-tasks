# сериализация


import json

data = {
    "fname": "Vadim",
    "lname": "Liubin",
    "age": 37,
    "hobbies": [
        "writer",
        "poetry",
        "books"
    ]
}

json_data = json.dumps(data)
print(json_data)

with open('data/output.json', "w") as file:
    json.dump(data, file)