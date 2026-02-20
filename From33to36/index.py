# ------------------------------------- #
#       Assignment: From 026 to 032     #
# ------------------------------------- #
from typing import Any

print(bool("here"))
print(bool(10))
print(bool([1, 2]))
print(bool((1, 2)))
print(bool(0))
print(bool(None))
print(bool({}))
print(bool([]))
print(bool(""))

# ------------------------------------- #
print("-" * 50)

html = 80
css = 60
javascript = 70

# Needed Output
# True
print(html > 50 and css > 50 and javascript > 50)

# ------------------------------------- #
print("-" * 50)

num_one = 10
num_two = 20
num = 20

# Needed Output
# True
print(num > num_one)
# False
print(num > num_two and num > num_one)

# ------------------------------------- #
print("-" * 50)

num_one = 10
num_two = 20

result: Any = num_one + num_two

# Needed Output

# 30
print(result)
# 27000
result **= 3
print(result)
# 1000
result %= 26000
print(result)
# 200.0
result /= 5
print(result)
# <class 'str'>
result = str(result)
print(type(result))

# -------------------------------------- #
print("-" * 50)


