from flask import Flask, session, request

app = Flask(__name__)
app.secret_key = "greet_secret"

@app.route("/", methods=["GET", "POST"])
def set_name():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return "Saved! Go to <a href='/greet'>/greet</a>"
    return '<form method="POST">Name: <input name="username"><button>Save</button></form>'

@app.route("/greet")
def greet():
    user = session.get("username", "Guest")
    return f"<h2>Hello, {user}!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
