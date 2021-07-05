from flask_restplus import Resource

from docker_mysql_mongod_sqs_s3.src.app import mongo


class ProductRoute(Resource):
    def get(self):
        count = mongo.db.count.find_one({"counter_name": "himanshu"})
        if not count:
            mongo.db.count.insert({"counter_name": "himanshu", "counter_value": 1})
        else:
            mongo.db.count.update({"counter_name": "himanshu"},
                                  {"$set": {"counter_value": count.get('counter_value') + 1}})
            count = mongo.db.count.find_one({"counter_name": "himanshu"})
        print(count)
        return count['counter_value']

    def post(self):
        count = mongo.db.count.find_one({"counter_name": "himanshu"})
        if not count:
            mongo.db.count.insert({"counter_name": "himanshu", "counter_value": 1})
        else:
            mongo.db.count.update({"counter_name": "himanshu"},
                                  {"$set": {"counter_value": count.get('counter_value') + 1}})
        print(count)
