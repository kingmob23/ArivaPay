from flask import Flask, render_template
from flask_admin import Admin

app = Flask(__name__, static_url_path='/static', static_folder='static')

# set optional bootswatch theme
app.config["FLASK_ADMIN_SWATCH"] = "cerulean"

admin = Admin(app, name="adminpage", template_mode="bootstrap3")
# Add administrative views here


@app.route("/")
def hello_world():
    return "<p>MAIN PAGE</p>"


@app.route("/auth")
def auth_page():
    return render_template("auth.html")
