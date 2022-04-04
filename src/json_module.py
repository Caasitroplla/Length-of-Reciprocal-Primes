import json

# saves a dictionary to the json file
def save_data(dict, filename='data.json'):
	with open(filename, 'w') as json_file:
		json.dump(dict, json_file)

# gets the data stored in the json file
def get_data(filename='data.json'):
	with open(filename, 'r') as json_file:
		data = json.load(json_file)
	return data 