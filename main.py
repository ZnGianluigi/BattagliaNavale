from flask import Flask,jsonify,request

app = Flask("main")

@app.route("/")
def index():
    return app.send_static_file("index.html")  #flask vuole che i file static siano in una cartella a parte

app.run('0.0.0.0',port=80)