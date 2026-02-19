# ------------------------------------- #
#       Assignment: From 021 to 023     #
# ------------------------------------- #

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
print(friends[0])
# "Osama" => Method Two
print(friends[-5])
# "Mahmoud" => Method One
print(friends[-1])
# "Mahmoud" => Method Two
print(friends[4])

# ------------------------------------- #

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama", "Sayed", "Mahmoud"
print(friends[::2])
# "Ahmed", "Ali"
print(friends[1::2])

# ------------------------------------- #

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
print(friends[1:4])
# "Ali", "Mahmoud"
print(friends[-1:-3:-1])

# ------------------------------------- #

friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.append("Salem")
print(friends)

# ------------------------------------- #
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
friends.remove("Nasser")
friends.remove("Osama")
print(friends)
# ["Ahmed", "Sayed"]
friends.pop()
print(friends)

# ------------------------------------- #

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

# ------------------------------------- #
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
print(sorted(friends))
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
print(sorted(friends, reverse=True))

# ------------------------------------- #
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# 6
print(len(friends))

# ------------------------------------- #
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Needed Output
# Django
print(technologies[-1][0])
# Web
print(technologies[-1][-1])

# ------------------------------------- #
