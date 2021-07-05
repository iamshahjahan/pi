from flask_pymongo import PyMongo
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@127.0.0.1:3308/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config["MONGO_URI"] = "mongodb://localhost:27017/shopify_products"

api = Api(app)
mongo = PyMongo(app)
db = SQLAlchemy(app)

if __name__ == '__main__':
    from docker_mysql_mongod_sqs_s3.src.user.product_resource import ProductRoute
    from docker_mysql_mongod_sqs_s3.src.model.user import User
    from docker_mysql_mongod_sqs_s3.src.user.user_routes import UserResource

    db.session.query(User).delete()
    db.session.commit()
    api.add_resource(UserResource, "/user")
    api.add_resource(ProductRoute, "/product")
    app.run(port=8005, debug=True)
