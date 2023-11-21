from flask_login import LoginManager, UserMixin, login_user
from werkzeug.security import check_password_hash

from . import main


@main.route("/")
def index_page():
    return "<p>Main Page</p>"


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


@app.route("/login", methods=["GET", "POST"])
def login():
    # Handle login with form submission here
    username = request.form.get("username")
    password = request.form.get("password")
    admin = Admin.query.filter_by(username=username).first()
    if admin and check_password_hash(admin.password, password):
        login_user(admin)
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("login.html")


@main.route("/account")
def account_page():
    return "<p>Personal Account</p>"
