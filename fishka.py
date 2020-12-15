from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/bakha/")
def hello_bakha():
    return render_template("bakha.html")

@app.route("/dad/")
def hello_dad():
    return render_template("dad.html")

@app.route("/mom/")
def hello_mom():
    return render_template("mom.html")

@app.route("/dimash/")
def hello_dimash():
    return render_template("dimash.html")


@app.route("/<name>/")
def hello_bye(name):
    return f"Привет {name}, и проваливай!"

@app.route('/bakha/')
def comment_like(id):
    comment = Comment.query.get_or_404(id)
    comment.like += 1
    db.session.add(comment)
    db.session.commit()
    return jsonify({'likes': comment.like})

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0")
