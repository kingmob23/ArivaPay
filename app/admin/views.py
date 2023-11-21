from flask import redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from app.models import User, Admin


class MyModelView(ModelView):
    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect("login")


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect("login")
