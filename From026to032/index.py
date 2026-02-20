# ------------------------------------- #
#       Assignment: From 026 to 032     #
# ------------------------------------- #
from typing import Any

my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
unique_list = list(set(my_list))
print(unique_list)
# <class 'list'>
print(type(unique_list))
# 1, 2, 3, 4
unique_list.pop()
print(unique_list)

# ------------------------------------- #
print("-" * 50)

nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
print(nums.union(letters))
# {1, 2, 3, "A", "B", "C"}
print(nums | letters)
# {1, 2, 3, "A", "B", "C"}
print(nums ^ letters)
print(nums.symmetric_difference(letters))

# ------------------------------------- #
print("-" * 50)

my_set: set[Any] = {1, 2, 3}
letters_new: set[Any] = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
print(my_set.difference(letters_new))
# set()
my_set.intersection_update(letters_new)
print(my_set)
# {"A", "B"}
my_set.add("A")
my_set.add("B")
my_set.discard("C")
print(my_set)
# ------------------------------------- #
print("-" * 50)


set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output
# True
print(set_one.issubset(set_two))

# -------------------------------------- #

# Create Dictionary Here
my_dict = {
    "HTML": 90,
    "CSS": 80,
    "Python": 30,
    "AI": 20
}
# Needed Output

# "HTML Progress Is 90%"
print(f"HTML Progress Is {my_dict['HTML']}%")
# "CSS Progress Is 80%"
print(f"CSS Progress Is {my_dict['CSS']}%")
# "Python Progress Is 30%"
print(f"Python Progress Is {my_dict['Python']}%")
# "AI Progress Is 20%"
print(f"AI Progress Is {my_dict['AI']}%")