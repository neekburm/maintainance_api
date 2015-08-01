import json

maintenance_json_by_miles = {}
maintenance_json_by_months = {}
FILE_NAME = "toyota_maintenance.json"
with open("edmunds_data/" + FILE_NAME, 'r') as fp:
	maintenance_json = json.load(fp)

for action in maintenance_json["actionHolder"]:
	action_miles = action["intervalMileage"]
	if action["frequency"] == 4: # 1-time event
		if action_miles not in maintenance_json_by_miles:
			maintenance_json_by_miles[action_miles] = []
		maintenance_json_by_miles[action_miles].append([action["item"], action["itemDescription"], 4])
	if action["frequency"] == 3: # recurring event
		multiplier = 1
		while(action_miles * multiplier <= 300000):
			action_miles = action_miles * multiplier
			if action_miles not in maintenance_json_by_miles:
				maintenance_json_by_miles[action_miles] = []
			maintenance_json_by_miles[action_miles].append([action["item"], action["itemDescription"], 3])
			multiplier += 1
	

print(sorted(maintenance_json_by_miles.items()))