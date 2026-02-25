# ------------------------------------- #
# ----- Assignment: From 072 to 075 --- #
# ------------------------------------- #
from functools import reduce

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# def remove_chars(string: str) -> str:
#     return string[1:-1]

# clean_list = list(map(remove_chars, friends_map))
clean_list = list(map(lambda name: name[1:-1], friends_map))

for name in clean_list:
    print(name)

# Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"

# -------------------------------------- #
print('-' * 50)

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names(name: str) -> bool:
    return name[-1] == "m"

names = filter(get_names, friends_filter)

for name in list(names):
    print(name)

# print(get_names(friends_filter[0], 'm'))
# Output
# "Wessam"
# "Essam"

# -------------------------------------- #
print('-' * 50)

nums = [2, 4, 6, 2]

result_of_multiplication = reduce(lambda x, y: x * y, nums)

print(result_of_multiplication)

# Output
# 96

# -------------------------------------- #
print('-' * 50)

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for count, skill in enumerate(reversed(skills), start=50):
    if type(skill) == int:
        continue
    else:
        print(f"{count} - {skill}")

# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"