import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465  # For starttls
sender_email = "fads@gmail.com"
password = "fasd"

receiver_email = "czCZ@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""


def send_mail():
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            r = server.sendmail(sender_email, receiver_email, message)
            print(r)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)


if __name__ == "__main__":
    for i in range(1000):
        send_mail()
