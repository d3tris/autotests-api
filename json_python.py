import json

json_data = """
{
  "key": "value",
  "name": "Adele",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing",
    {
      "name": "Ariel"
    }
  ],
  "address": {
    "city": "Boston",
    "zip": "010101",
    "point": {
      "name": "Alise"
    }
  }
}
"""
parsed_data = json.loads(json_data)
print(parsed_data, type(parsed_data))

data = {
    'name': 'Ameli',
    'age': 30,
    'is_student': True
}
json_string = json.dumps(data, indent=2)
print(json_string, type(parsed_data))

with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)