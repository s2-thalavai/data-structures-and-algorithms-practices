import datetime

## Get the current date
today = datetime.date.today()

## Get the weekday of the current date
weekday = today.weekday()

print(f"Today is a {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][weekday]}")

