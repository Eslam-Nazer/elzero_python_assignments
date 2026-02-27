# ------------------------------------- #
# ----- Assignment: From 086 to 089 --- #
# ------------------------------------- #
from PIL import Image
"""
description: this file to solve assignments
"""

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    my_data.append("".join(data))

final_string = "".join(my_data).capitalize()

print(final_string) # Elzero

# --------------------------------- #
print('=' * 50)

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # if type(item1) is str: # solution one
    #     my_data.append(item1)
    if isinstance(item1, str): # solution two
        my_data.append(item1)

# print(my_data)
final_string_two = "".join(my_data).capitalize()
print(final_string_two)

# --------------------------------- #
print('=' * 50)

im = Image.open("./elzero-pillow.png")

box = (400, 0, 800, 400)
region = im.crop(box).convert("L")

# region.show()

box = (0, 400, 1200, 800)
region_two = im.crop(box).convert("L").rotate(angle=180)

# region_two.show()

# --------------------------------- #
print('=' * 50)

def say_hello_to(name):
    """
    :param name: parameter(someone) => Person Name
    :return: message with say hello to name
    :description: Function To Say Hello To Anyone
    """
    return f"Hello, {name}!"

print(say_hello_to("Osama"))
help(say_hello_to)
print('=' * 20)
print(say_hello_to.__doc__)

# --------------------------------- #
print('=' * 50)

MY_FRIENDS = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> None:
    """
    :param some_peoples:
    :return: None
    """
    for some_one in some_peoples:
        print(f"Hello {some_one}")

say_hello(MY_FRIENDS)
