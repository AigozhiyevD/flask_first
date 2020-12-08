from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Эта страница <h1>Домашняя!!!!!!!!!!!<h1>"

@app.route("/bakha/")
def hello_bakha():
    return "ТЫ <h1>ЖБ) <h1>"

@app.route("/<name>/")
def hello_bye(name):
    return f"Привет {name}, и проваливай!"

if __name__ == "__main__":
    app.run()
