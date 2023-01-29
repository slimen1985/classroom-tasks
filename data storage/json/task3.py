import json
import datetime

data = {
    "fname": "Vadim",
    "lname": "Liubin",
    "birthday": datetime.date(1985, 8, 7),
    "hired_at": datetime.datetime(2023, 9, 29, 12, 30, 5),
    "hobbies": [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}


class DateFormatEncoder(json.JSONEncoder):

    def to_default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'value': obj.strftime('%d/%m/%y %H:%M:%S'),
                'datetime': True
            }
        elif isinstance(obj, datetime.date):
            return {
                'value': obj.strftime('%d/%m/%y'),
                'date': True
            }
        return json.JSONEncoder.default(self, obj)


json_data = json.dumps(data, cls=DateFormatEncoder, indent=4, default=str)
print(json_data)
