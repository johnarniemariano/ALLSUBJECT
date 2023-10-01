from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/favorites")
def favorites():
    return render_template("favorites.html")

@app.route("/friends")
def friends():
    return render_template("friends.html")

@app.route("/family")
def family():
    return render_template("family.html")

if __name__ == '__main__':
    app.run(debug=True)
