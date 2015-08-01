import json

with open('makes.json', 'r') as input:
	makes = json.load(input)

with open('makes.json', 'w') as out:
	json.dump(makes, out, sort_keys=True, indent=4)