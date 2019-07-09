"""
high level support for rending tamplates and use for bunisess logic
"""

import string
import os
import os.path
from flask import (Flask, flash, redirect, render_template, request,
                   session, url_for, jsonify, send_from_directory, send_file)
import json

app = Flask(__name__)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config['TEMPLATES_AUTO_RELOAD'] = True
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=["GET"])
def index_page():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
