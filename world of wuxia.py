from flask import Flask, render_template
# from jinja2 import Template
# import requests
# import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')




app.run()
