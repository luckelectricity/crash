import json

numbers = [2,3,4,5,6,7,8,9,10]

fileName = 'number.json'

with open('number.json', 'w') as file_obj:
  json.dump(numbers, file_obj)
