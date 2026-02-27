# ------------------------------------- #
# ----- Assignment: From 090 to 094 --- #
# ------------------------------------- #


# NUM = input("Add Your Number ").strip()
#
# if not NUM.isdigit():
#     raise Exception("Only Numbers Allowed")
# elif len(NUM) > 1:
#     raise IndexError("Only One Character Allowed")
# elif int(NUM) == 0:
#     raise ValueError("Number Must Be Larger Than 0")
# else:
#     print("=" * 20)
#     print(f"The Number Is {int(NUM)}")
#     print("=" * 20)

# ------------------------------------- #
print("=" * 50)

# try:
#     LETTER = input("Add Letter From A to Z: ")
#     if LETTER.__len__() > 1:
#         raise IndexError("You Must Write One Character Only")
#     elif LETTER.islower():
#         raise Exception("The Letter Not In A - Z")
#
# except IndexError as e:
#     raise e
# except Exception as e:
#     raise e
# else:
#     print(f"You Type {LETTER}")

# ------------------------------------- #
print("=" * 50)

def calculate(num1, num2) -> float:
  return num1 + num2

print(calculate(20, 30))


