# ------------------------------------- #
# ----- Assignment: From 076 to 078 --- #
# ------------------------------------- #

import random
import sys
import os
sys.path.append(os.path. dirname(os.path.realpath(__file__)) + os.sep +"python")
from my_mod import say_welcome as new_welcome

evenNumber = random.randrange(1, 9, 2)
number = random.randint(10, 50)
print(f"Random Number Between 10 And 50 => \"{number}\" Show The Random Number Here")

evenNumber = random.randrange(2, 10, 2)
print(f"Random Even Number Between 2 And 10 => \"{evenNumber}\" Show The Random Even Number Here")

oddNumber = random.randrange(1, 9, 2)
print(f"Random Odd Number Between 1 And 9 => \"{oddNumber}\" Show The Random Odd Number Here")

print(dir(random))

# -------------------------------------- #
print('-' * 20)

# my_mod.say_hello('Eslam')
# my_mod.say_welcome('Eslam')

# -------------------------------------- #
print('-' * 20)

# say_welcome('Eslam')

# -------------------------------------- #
print('-' * 20)

new_welcome('Eslam')