# -*- coding: utf-8 -*-
from flask import Flask, render_template
import os
print ("YOp")

path = os.path.abspath('.')
print ("XXX")
print (path)

app = Flask(__name__, static_url_path='/',  static_folder='/', template_folder=path)

@app.route("/index.html")
def hello():
    return render_template("index.html")

@app.route("/qualification.html")
def qualification():
    return render_template("qualification.html")

@app.route("/manifest.json")
def manifest():
    return app.send_static_file('manifest.json')

@app.route("/service-worker.js")
def serviceWorker():
    return app.send_static_file('service-worker.js')


if __name__ == "__main__":
    app.run(debug=True)