from flask import request, jsonify
from flask import current_app as app


@app.route('/vote', methods=['GET'])
def count_vote():
	# title = request.form.get("title")
	# content = request.form.get("content")
	# if (title is None and content is None):
		# return jsonify(error={"title": "this field is required", "content": "this field is required"}), 400
	# elif (title is None):
		# return jsonify(error={"title": "this field is required"}), 400
	# elif (content is None):
		# return jsonify(error={"content": "this field is required"}), 400
	# try:
		# message = Message(title=title, content=content)
		# db.session.add(message)
		# db.session.commit()
	return jsonify(id="Test"), 200
	# except Exception:
		# return jsonify(error="Can not add message to database"), 400


