import json

podatki = {

  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(podatki)

print(y)