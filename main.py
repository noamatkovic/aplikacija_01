# Python Flask aplikacija 

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")                                     #definira od kojih linkova će se sastojati stranica
def index():
    return render_template("index.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/onama")
def onama():
    return "Ovo je stranica O nama!"

if __name__ == "__main__":
    app.run(use_reloader=True)





