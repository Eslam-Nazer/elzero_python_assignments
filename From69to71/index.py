# ------------------------------------- #
# ----- Assignment: From 069 to 071 --- #
# ------------------------------------- #

values = (0, 1, 2)

if any(values):

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
# Because in if first it is true
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")

# Good
# ----------------------------------- #
print("-" * 50)

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

# ----------------------------------- #
print("-" * 50)

n = 20 # or 21 or 22

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good

# ----------------------------------- #
print("-" * 50)

def my_all(args):
    for arg in args:
        if not arg:
            return False
    return True

def my_any(args):
    for arg in args:
        if bool(arg):
            return True
    return False

def my_min(args):
    iterator = iter(args)
    smallest = next(iterator)
    for item in iterator:
        if item < smallest:
            smallest = item
    return smallest

def my_max(args):
    iterator = iter(args)
    biggest = next(iterator)
    for item in iterator:
        if item > biggest:
            biggest = item
    return biggest

# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False
#
# # my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False
#
# # my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100
#
# # my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700