from flask import Flask,jsonify,request

app = Flask("main")

@app.route("/")
def index():
    return "ciao!"

app.run('0.0.0.0',port=80)