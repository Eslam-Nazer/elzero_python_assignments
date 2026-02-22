# ------------------------------------- #
# ----- Assignment: From 056 to 059 --- #
# ------------------------------------- #

# ------------- 1 ---------------- #

def calculate(num1, num2, operation = "add"):
    operation = operation.strip().lower()
    if operation == "add" or operation == "a":
        return num1 + num2
    elif operation == "subtract" or operation == "s":
        return num1 - num2
    elif operation == "multiply" or operation == "m":
        return num1 * num2
    else:
        return "Invalid operation"

print(calculate(10, 20, "add"))
print(calculate(10, 20, "s"))
print(calculate(10, 20, "mULtiply"))
print(calculate(10, 20))
print(calculate(10, 20, "nnn"))

# ------------- 2 ---------------- #
print('-' * 20)

def addition(*nums):
    sum = 0
    for num in nums:
        if num == 10:
            continue
        elif num == 5:
            sum -=num
        else:
            sum += num
    return sum

print(addition(10, 20, 30, 10, 15, 5, 100))

# ------------- 3 ---------------- #
print('-' * 20)

def showSills(name, *skills):
    print(f"Hello {name} Your Skills: ")
    for skill in skills:
        print(f"- {skill}")

showSills("Osama", "HTML", "CSS", "JS", "Python")
showSills("Ahmed")

# ------------- 4 ---------------- #
print('-' * 20)

def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"

print(say_hello("Osama", 38, "Egypt"))
print(say_hello())