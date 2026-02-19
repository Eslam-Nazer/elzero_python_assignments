# ------------------------------------- #
#       Assignment: From 011 to 018     #
# ------------------------------------- #

name = "John"
age = 36
country = "Egypt"

print(
    f'"Hello \'{name}\', How You Doing \\ """ Your Age Is "{age}"" + And Your Country Is: {country}'
)
# ------------------------------------- #

print(
    f'"Hello \'{name}\', How You Doing \\\n """ Your Age Is "{age}"" + \n And Your Country Is: {country}'
)
# ------------------------------------- #
name = "Elzero"

print(f'Second Letter Is "{name[1]}"')
print(f'Third Letter Is "{name[2]}"')
print(f'Last Letter Is "{name[-1]}"')

# ------------------------------------- #

name = "#@#@Elzero#@#@"
print(name.strip("#@"))

# ------------------------------------- #
size = 4
num = "9"
print(num.zfill(size))
num = "15"
print(num.zfill(size))
num = "130"
print(num.zfill(size))
num = "950"
print(num.zfill(size))
num = "1500"
print(num.zfill(size))

# ------------------------------------- #

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# ------------------------------------- #

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

# ------------------------------------- #

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

# ------------------------------------- #

name = "Elzero"

# Needed Output
# 2
print(name.index("z"))

# ------------------------------------- #

msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School
print(msg.replace("<3", "Love", 1))

# ------------------------------------- #
msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although Love Elzero Web School
print(msg.replace("<3", "Love"))

# ------------------------------------- #

name = "Osama"
age = 38
country = "Egypt"

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt

print(f" My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

# ------------------------------------- #
