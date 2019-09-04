import requests
import smtplib
import time
import sys
import os
import datetime
import calendar
import pytz
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
n = 0

def email_sent(to):
  fromaddr = 'YOUR EMAIL'
  toaddrs  = to #EMAIL TO SEND
  pwd = "ACCOUNT PASSWD"
  msg = MIMEMultipart('alternative')
  msg['From'] = 'FROM'
  msg['To'] = to
  msg['Subject'] = 'To Whom It May Concern: ' + local.strftime("%a, %b %d, %Y")
  body = """
  testing testing
  """
  msg.attach(MIMEText(body, 'plain'))
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.ehlo()
  server.starttls()
  server.login(fromaddr, pwd)
  text = msg.as_string()
  server.sendmail(fromaddr, toaddrs, text)
  server.quit()
  print(':SERVER: Email Sent to: ' + to + '!')

def countdown():
  global n
  global then
  global local
  global my_date
  global weekend
  global fdate
  then = datetime.datetime.now(pytz.utc)
  local = then.astimezone(pytz.timezone('America/Los_Angeles'))
  my_date = date.today()
  weekday = calendar.day_name[my_date.weekday()]
  fdate = str(local.strftime("%Y-%m-%d"))
  sys.setrecursionlimit(1000 + n)
  current_time = str(local.strftime("%I:%M %p"))
  if current_time == '01:00 AM':
    email_sent('TO ADDR')
    n += 1
    time.sleep(45)
    countdown()
  else:
    n += 1
    time.sleep(45)
    countdown()


countdown()
