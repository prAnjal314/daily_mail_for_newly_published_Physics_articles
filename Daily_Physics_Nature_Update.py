# --Pranjal Das-- #

from email.message import EmailMessage
import smtplib
import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta

####--Define send_email function--####
def send_email(recipient, subject, body):
    for i in range(len(recipient)):
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = SENDER
        msg["To"] = recipient[i]
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER, PASSWORD)
        server.send_message(msg)
        server.quit()

recipients = ["<recipient_1_mail_address>", "<recipient_2_mail_address>"]
today = date.today()
yesterday = today - timedelta(days=1)
List = []

####--Srapping Part--####
URL = 'https://www.nature.com/subjects/physics/nature'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('ul', class_='ma0 mb-negative-2 clean-list')
topics = results.find_all('li', class_='border-gray-medium border-bottom-1 pb20 mt20')

#####--Getting Main Content--#####
for a in topics:
    time = a.find('time', itemprop='datePublished').get('datetime')
    if time == str(today) or time ==str(yesterday):         #Check publishing date of the Article
        tmp = a.find_all('span', itemprop='name')           #Get the Authors' names
        authors = '|'
        for b in tmp:
            authors += b.text + '|'

        title = a.find('h3', itemprop='name headline')      #Get the title of the article
        link = a.find('a', itemprop='url').get('href')      
        description = a.find('div', itemprop='description')
        List.append([title.text.strip(), description.text.strip(), time, authors, link])

####--Login details--####
SENDER = "<sending mail address>"
PASSWORD = "<sender password>" #open("user_details.txt", "r")

####--Body of the mail--####
body = ""
for i in range(len(List)):
    body += "[{a}] {title}\n{description}\n{date}\n{authors}\n{link}\n\n".format(a=i+1, title="Title: "+List[i][0], description="description: "+List[i][1], date="Date: "+List[i][2], authors="Authors: "+List[i][3], link="Link: "+List[i][4])

body += "\n Have a nice day!"
if body != "\n Have a nice day!":
    send_email(recipients, subject="Hello, Here Are Some Interesting News for You", body=body)