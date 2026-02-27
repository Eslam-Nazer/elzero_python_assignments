# ------------------------------------- #
# ----- Assignment: From 079 to 080 --- #
# ------------------------------------- #

from datetime import datetime

specific_datetime = datetime(2021, 6, 25)

print(f"Days From 2021-06-25 To now Is => {(datetime.today() - specific_datetime).days}")

# ------------------------------------ #
print('-' * 50)

print(datetime.now().strftime("%Y-%m-%d"))
print('-' * 10)
print(datetime.now().strftime("%b %d, %Y "))
print('-' * 10)
print(datetime.now().strftime("%d / %b / %y "))
print('-' * 10)
print(datetime.now().strftime("%d / %B / %Y"))
print('-' * 10)
print(datetime.now().strftime("%a, %d %B %Y "))
print('-' * 10)