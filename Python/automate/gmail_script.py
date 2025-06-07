import schedule
import webbrowser
import time

def open_gmail():
    Url = 'https:mail.google.com'
    webbrowser.open(url)

schedule.every().day.at("10:00").do(open_gmail)

while True:
    schedule.run_pending()
    time.sleep(1) 