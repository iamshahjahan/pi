from docker_mysql_mongod_sqs_s3.src.app import db
from docker_mysql_mongod_sqs_s3.src.model.user import User


class UserController:
    def insert(self, username, email):
        session = db.session
        try:
            me = User(username, email)
            session.add(me)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        print("in main")

