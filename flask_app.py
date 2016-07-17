import json
import os

from flask import Flask

from db import get_records

app = Flask(__name__)

@app.route("/")
def index():
    return json.dumps(get_records())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)