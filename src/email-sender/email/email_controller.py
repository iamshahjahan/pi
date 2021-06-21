from tasks import send_mail_async


def call_send_mail():
    send_mail_async.delay()


if __name__ == "__main__":
    for i in range(1000):
        call_send_mail()

