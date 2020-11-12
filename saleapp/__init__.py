from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


app = Flask(__name__)
app.secret_key = '8972^&*A*(*&A*S(D*A()SD*kjahsđ12738712'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/saledb3?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app=app)
admin = Admin(app=app, name='Quan ly', template_mode='bootstrap4')