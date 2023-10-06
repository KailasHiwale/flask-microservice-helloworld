from flask import Flask
from flask_cors import CORS
import json


app = Flask(__name__)

CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/", methods=["GET"])
def info():
	return json.dumps({"msg": "hello world"})


if __name__=="__main__":
	app.run(host="0.0.0.0", port="5001")
