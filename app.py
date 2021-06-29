# serve.py

from flask import Flask, request, redirect
from flask import render_template
from flask_cors import CORS
from db.models import register_link, get_link

# creates a Flask application, named app
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# a route where we will display a welcome message via an HTML template


@app.route("/")
def main():
	return render_template('index.html')


@app.route("/registerLink", methods=['GET', 'POST'])
def cadLink():
	response = request.get_json()
	link = response.get("link")
	index = register_link(link)
	return {"status_code": 200, "index": index}


@app.route("/<index>")
def return_link(index):
	url = get_link(index)
	if len(url)==0:
		return render_template("erro.html")

	return redirect(url[0]["url"], code=302)


# run the application
if __name__ == "__main__":
	app.run(debug=True)
