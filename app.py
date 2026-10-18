from flask import Flask, render_template, request, redirect, url_for 
from dfa import LoginDFA

app = Flask(__name__)

dfa = LoginDFA()

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "admin123"


@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if dfa.state == "LOCKED":
            message = "Account is locked. No further attempts allowed."

        elif username == CORRECT_USERNAME and password == CORRECT_PASSWORD:

            state = dfa.process("C")
            message = "Login successful!"

        else:

            state = dfa.process("F")

            if state == "ONE_FAIL":
                message = "Wrong password. 1 failed attempt."

            elif state == "TWO_FAIL":
                message = "Wrong password. 2 failed attempts."

            elif state == "LOCKED":
                message = "Account locked after 3 consecutive failures."

    return render_template(
        "index.html",
        state=dfa.state,
        message=message
    )


@app.route("/reset", methods=["POST"])
def reset():

    dfa.reset()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)