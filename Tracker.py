import requests
from bs4 import BeautifulSoup
import smtplib

#sending and email to your email
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("Username", "password")
    subject = "Camera Price is Down!"
    body =  " Check the link for the price drop"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "from email"
        "reciever email"
    )
    server.quit()

URL = 'https://www.amazon.de/-/en/Canon-EOS-Housing-Adapter-EF-EOS/dp/B07NJJ59J4/ref=sr_1_1?dchild=1&keywords=canon+eos+rp&qid=1613844878&sr=8-1'

headers = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[0:9])

if(converted_price < 1200.00):
    send_mail()

