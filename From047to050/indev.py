# ------------------------------------- #
# ----- Assignment: From 041 to 046 --- #
# ------------------------------------- #
from math import frexp

from From011to018.index import size

# ----- 1 ----- #
# num = int(input("Enter a number: ").strip())
# count = 0
#
# if num < 0:
#     print(f"Number {num} Is Not Larger Than 0")
# else:
#     while num > 0:
#         num -= 1
#         if num == 0 or num == 6:
#             continue
#         print(num)
#         count += 1
#     else:
#         print(f"{count} Numbers Printed Successfully.")

# ---------------- 2 ------------------ #
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
i = 0
count = 0
while i < len(friends):
    friend = friends[i]
    i += 1
    if not friend.islower():
        print(friend)
    else:
        count += 1
        continue
else:
    print(f"Friends Printed And Ignored Names Count Is {count}")

# ---------------- 3 ------------------ #
print("-" * 50)

# Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0))

# Needed Output
# "HTML"
# "CSS"
# "JavaScript"
# "PHP"
# "Python"

# ---------------- 4 ------------------ #
print("-" * 50)

my_friends = []

while len(my_friends) < 4:
    friend = input("Enter your friend's name: ").strip()

    if friend.isupper():
        print("Invalid Name")
        continue
    else:
        if friend.islower():
            friend = friend.title()
            print(f"Friend {friend} Added => 1st Letter Become Capital")
        else:
            print(f"Friend {friend} Added")
        my_friends.append(friend)
        print(f"Names Left in List Is {4 - len(my_friends)})")
else:
    print(my_friends)
