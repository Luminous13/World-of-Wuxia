from flask import Flask, render_template, requests


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')




app.run()
