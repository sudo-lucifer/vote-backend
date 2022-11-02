from flask import request, jsonify
from flask import current_app as app

names = {}

@app.route('/vote', methods=['POST'])
def count_vote():
	input_name = request.form.get("name")
	if (input_name is None):
		return jsonify(error={"name": "this field is required"}), 400
	if input_name in names.keys():
		names[input_name] += 1
	else:
		names[input_name] = 1
	return jsonify({"name": input_name}), 200

@app.route('/tally', methods=['GET'])
def get_votes():
	print(names)
	return jsonify(names), 200
