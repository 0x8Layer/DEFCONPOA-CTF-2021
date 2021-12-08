import urllib
from base64 import b64encode
from flask import Flask, g, render_template, redirect, url_for, request, flash, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = "4s3cr3t"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin", methods=["GET"])
def admin():
    try:
        auth = int(request.cookies.get("auth"))
    except:
        auth = 0
    if auth != 1:
        resp = make_response(render_template("index.html"))
        resp.set_cookie("auth", b'0')
        return resp

    return render_template("admin.html")

@app.route("/show", methods=["POST"])
def show():
    try:
        auth = int(request.cookies.get("auth"))
    except:
        auth = 0
    if auth != 1:
        resp = make_response(render_template("index.html"))
        resp.set_cookie("auth", b'0')
        return resp
    try:
        url = request.form.get("url")
        content = urllib.request.urlopen(url).read()
    except:
        content = b""
    return render_template("admin.html", content=b64encode(content).decode())

if __name__ == "__main__":
    app.run()
