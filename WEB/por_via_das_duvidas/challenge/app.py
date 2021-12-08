import os
import hashlib
import sqlite3
from binascii import hexlify, unhexlify
from flask import Flask, g, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from Crypto.Cipher import AES


app = Flask(__name__)
app.config['SECRET_KEY'] = "generate-a-s3cr3t"

login_manager = LoginManager()
login_manager.init_app(app)

DATABASE = "db.sqlite"

class User(UserMixin):
    def __init__(self, id, email, username, password):
        self.id = str(id)
        self.email = email
        self.username = username
        self.password = password
        self.authenticated = False

    def is_active(self):
        return self.is_active()

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def get_id(self):
        return self.id

class AESCipher(object):
    def __init__(self):
        self.key = os.environ['FLAG']
        self.cipher = AES.new(self.key.encode('utf-8'), AES.MODE_ECB)
        self.BLOCK_SIZE = 16
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)*chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)
        self.unpad = lambda s: s[:-ord(s[len(s)-1:])]

    def encrypt(self, text):
        text = self.pad(text).encode('utf-8')
        return hexlify(self.cipher.encrypt(text))

    def decrypt(self, enc):
        return self.unpad(self.cipher.decrypt(unhexlify(enc)))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@login_manager.user_loader
def load_user(user_id):
    result = query_db("SELECT rowid,* FROM users WHERE rowid = (?)", [user_id])[0]
    if result is None:
        return None
    else:
        return User(int(result[0]), result[1], result[2], result[3])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        remember_me = True if request.form.get("remember_me") else False
        result = get_db().execute("SELECT rowid,* FROM users WHERE email ='" + email + "'")
        result = result.fetchall()[0]
        user = load_user(result[0])
        if email == user.email and hashlib.md5(password.encode()).hexdigest() == user.password:
            login_user(user, remember=remember_me)
            return redirect(url_for("profile"))
        else:
            flash("Por favor, verifique suas credenciais.")
            return redirect(url_for("login"))

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)

@app.route("/encrypt", methods=["GET"])
@login_required
def encrypt():
    text = request.args.get('text')
    if text == None:
        return '''<p>?????</p>'''
    if len(text) > 16:
        return redirect(url_for("profile"))
    return '''<p>{}</p>'''.format(AESCipher().encrypt(text).decode())

@app.route("/execute", methods=["GET", "POST"])
@login_required
def execute():
    permission = request.cookies.get('perm')
    if permission is not None and current_user.username == "admin":
        decoded_perm = AESCipher().decrypt(permission).decode()
        if decoded_perm == "execution_exec_ok":
            command_encoded = request.form.get('cmd')
            if command_encoded is None: return '''<p></p>'''
            command_decoded = AESCipher().decrypt(command_encoded).decode()

            if len(command_decoded) > 3: return '''<p></p>'''

            return '''{}'''.format(os.popen(command_decoded).read())
    return '''<p>Você não tem permissão para executar comandos.</p>'''

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=False)
