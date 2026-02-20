# ------------------------------------- #
# ----- Assignment: From 041 to 046 --- #
# ------------------------------------- #
from supervisor.medusa.filesys import months

# ----- 1 ----- #

# num1 = int(input("Enter First Numer : ").strip())
# num2 = int(input("Enter Second Numer : ").strip())
#
# operation = input("Enter Operation \"+\" | \"-\" | \"*\" | \"/\" | \"%\" : ").strip()
#
# if operation == "+":
#     print(f"result: {num1 + num2}")
# elif operation == "-":
#     print(f"result: {num1 - num2}")
# elif operation == "*":
#     print(f"result: {num1 * num2}")
# elif operation == "/":
#     print(f"result: {num1 / num2}")
# elif operation == "%":
#     print(f"result: {num1 % num2}")
# else:
#     print(f"Operation {operation} not supported")

# ------------------------------------------- #
print("-" * 50)

# ----- 2 ----- #

# age = 17
# print("App Is Suitable For You" if age >= 6 else "App Is Not Suitable For You")

# ------------------------------------------- #
print("-" * 50)

# age = int(input("What is your age? ").strip())
#
# if 10 <= age <= 100:
#     months = age * 12
#     days = age * 365
#     print(f"Your Age In Months Is {months} Months")
#     print(f"Your Age In Days Is {days} Days")
# else:
#     print("Sorry, your age must be between 10 and 100.")

# ------------------------------------------- #
print("-" * 50)

country = input("Input Your Country : ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country.upper() in ["KSA", "USA"]:
    country = country.upper()

if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is {price}")