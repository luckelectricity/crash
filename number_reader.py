import json

fileName = 'number.json'

with open(fileName) as file_obj:
  numbers = json.load(file_obj)

print(numbers)
