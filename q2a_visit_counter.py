from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def counter():
    visits = int(request.cookies.get("visits", 0)) + 1
    resp = make_response(f"<h2>You have visited {visits} times</h2>")
    resp.set_cookie("visits", str(visits))
    return resp

if __name__ == "__main__":
    app.run(debug=True)
