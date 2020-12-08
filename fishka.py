from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bakha/")
def hello_bakha():
    return render_template("bakha.html")

@app.route("/<name>/")
def hello_bye(name):
    return f"Привет {name}, и проваливай!"

if __name__ == "__main__":
    app.run()
