from flask import Flask
from flask_admin import Admin

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='adminpage', template_mode='bootstrap3')
# Add administrative views here

@app.route("/")
def hello_world():
    return "<p>MAIN PAGE</p>"