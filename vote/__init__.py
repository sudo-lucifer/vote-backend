from flask import Flask


def create_app():
	app = Flask(__name__, instance_relative_config=True)

	with app.app_context():
		from . import apis
	return app


if __name__ == '__main__':
	app = create_app()
	app.run(host='0.0.0.0')
