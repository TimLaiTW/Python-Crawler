# Python-Crawler

#### [Trails infomation of different ski resorts at New England area](https://github.com/TimLaiTW/Python-Crawler/tree/master/Ski_Resort_Level_Count)
Some basic commands in BeautifulSoup, requests and io. 

#### [Stock Price Tracking](https://github.com/TimLaiTW/Python-Crawler/tree/master/Stock_Price_Tracking)
Send notification email if the stock price goes lower than the setting price.
Utilize 'smtplib' to complete the mail sending function(ignoring some variable initialization):
```ruby
def send_mail(title, price):
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
