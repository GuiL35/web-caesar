from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!doctype html>

<html>
	<head>
		<style>
			form {{
				background-color: #eee;
				padding: 20px:
				margin: 0 auto;
				width: 540px;
				font: 16px sans-serif;
				border-radius: 10px;
			}}
			textarea {{

				margin: 20px;
				width: 500px;
				height: 120px;
			}}
			#button{{
				margin-left: 20px;
				margin-bottom: 20px;
			}}
			label{{
				margin: 20px;
			}}
		</style>
	</head>
	<body>
		<form action = "/" method = "POST">
			<label for="rot"> Rotate by:</label>
			<input id="rot" type="text" name = "rot" value = "0" />
			<textarea name="text" id="text">{0}</textarea>
			<input type="submit" id = "button" />
		</form>
	</body>
</html>
"""

@app.route("/")
def index():
	return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
	new_text = request.form['text']
	new_rot = int(request.form['rot'])
	return form.format(rotate_string(new_text,new_rot))


app.run()