from celery import Celery

from send_email import send_mail

app = Celery('tasks', broker='pyamqp://guest@localhost//',
             backend="backend")

@app.task
def send_mail_async():
    return send_mail()
