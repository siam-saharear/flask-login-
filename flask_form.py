

from flask import Flask,render_template,request,session,url_for,redirect
import random 
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "1234"
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route("/login/",methods = ["POST","GET"])
def login_func():
    if request.method == "POST":
        session.permanent = True
        session["user"] = request.form["user"]
        session["password"] = request.form["password"]
        return redirect(url_for("user_func"))

    else:
        if "user" in session:
            return redirect(url_for("user_func"))

        return render_template("login.html")


@app.route("/user")
def user_func():
    if "user" in session:
        user = session["user"] 
        return render_template("user.html",user = user)
    return redirect(url_for("login_func"))

@app.route("/logout")
def logout_func():
    session.pop("user",None)
    return redirect(url_for("login_func"))




if __name__=="__main__":
    Flask.debug = True
    app.run()
