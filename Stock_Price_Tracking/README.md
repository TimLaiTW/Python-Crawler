# Stock Price Tracking
Tracking the specific stock price, and send the notification email if it goes lower than the setting price.

Send_mail function with arguments:

```ruby
def send_mail(title, price):
    user_account = '...'
    user_pawssword = '...'
    reveiver_account = '...'

    subject = "%s PRICE DOWN!!!" % title
    body = "%s down to %s!" % (title, price)
    msg = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user_account, user_password)
    server.sendmail(user_account, receiver_account, msg)
    server.close()
```
