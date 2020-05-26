import smtplib
import requests
from bs4 import BeautifulSoup

def send_mail(title, price):
    gmail_user = 'user_account'
    gmail_pswd = 'user_password'
    sent_from = gmail_user
    to = 'receiver_account' # could be a list too

    subject = "%s PRICE DOWN!!!" % title
    body = "%s down to %s!" % (title, price)
    msg = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_user, gmail_pswd)
    server.sendmail(sent_from, to, msg)
    print('Hey mail has been sent!')
    server.close()

stock_URL = 'https://finance.yahoo.com/quote/tsla?ltr=1'
page = requests.get(stock_URL)
soup = BeautifulSoup(page.text, 'html.parser')

title = soup.find('h1', {'class':'D(ib) Fz(16px) Lh(18px)'}).get_text()
price = soup.find('span', {'class':'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'}).get_text()
converted_price = float(price[0:6])

if(converted_price < 820.00):
    send_mail(title, price)


