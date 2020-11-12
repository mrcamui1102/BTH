from saleapp import admin, db
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category, Products
from flask_admin import BaseView, expose


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')


admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Products, db.session))
admin.add_view(ContactView(name='Lien He'))
