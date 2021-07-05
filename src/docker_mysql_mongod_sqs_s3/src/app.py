from flask_sqlalchemy import SQLAlchemy
import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@127.0.0.1:3308/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

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
