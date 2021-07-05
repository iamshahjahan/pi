from flask_sqlalchemy import SQLAlchemy
import werkzeug


werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@127.0.0.1:3308/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

db.drop_all()
db.create_all()
db.session.commit()

me = User('admin', 'admin@example.com')
db.session.add(me)
db.session.commit()
#
# peter = User.query.filter_by(username='admin').first()
# print(peter)

if __name__ == '__main__':
    app.run(port=8005, debug=True)
