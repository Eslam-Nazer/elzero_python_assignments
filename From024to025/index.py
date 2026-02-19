# ------------------------------------- #
#       Assignment: From 024 to 025     #
# ------------------------------------- #

name = ("John",)

print(name)
print(type(name))

# ----------------------------- #

friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
print(("Elzero",) + friends[1:])
# <class 'tuple'>
print(type(("Elzero",) + friends[1:]))
# 3 Elements
print(len(("Elzero",) + friends[1:]))

# ------------------------------------- #

nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements
nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(len(nums_and_letters_one))

# ------------------------------ #

my_tuple = (1, 2, 3, 4)

# Needed Output
a, b, _, c = my_tuple
# 1
# 2
# 4
print(a)
print(b)
print(c)