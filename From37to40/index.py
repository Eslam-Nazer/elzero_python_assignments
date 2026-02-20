# ------------------------------------- #
#       Assignment: From 037 to 040     #
# ------------------------------------- #

# name = input("What is your name? ").strip().capitalize()

# print(f"Hello {name}, Happy To See You Here.")

# -------------------------------------- #
print("-" * 50)

# age = int(input("What is your age? ").strip())

# Age_Value_If_Larger_Than_16 = bool(age > 16)

# print(Age_Value_If_Larger_Than_16)
# if not Age_Value_If_Larger_Than_16:
#     print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# else:
#     print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

# -------------------------------------- #
print("-" * 50)

# First_Name = input("What is your first name? ").strip().capitalize()
# First_Letter_From_Second_Name = input("What is your last name? ").strip().capitalize()

# print(f"Hello {First_Name} {First_Letter_From_Second_Name:.1}.")

# -------------------------------------- #
print("-" * 50)

email = input("What is your email? ").strip()

userName = email[:email.index("@")].capitalize()
domainName = email[email.index("@") + 1:email.index(".")].lower()
topLevelDomain = email[email.index(".") + 1:].lower()

print(f"Your Name Is {userName} \nEmail Service Provider Is {domainName} \n Top Level Domain Is {topLevelDomain}")
