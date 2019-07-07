"""
    Created on Sun July 7 14:58:57 2018
    @author: Kam
"""

import string
import os
import os.path
from flask import (Flask, flash, redirect, render_template, request,
                   session, url_for, jsonify, send_from_directory, send_file)
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'