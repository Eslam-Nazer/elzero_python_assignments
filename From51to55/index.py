# ------------------------------------- #
# ----- Assignment: From 051 to 055 --- #
# ------------------------------------- #

# -------------- 1 --------------- #
# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
final_list = []
while my_nums:
    num = my_nums.pop(0)
    if num  % 5 == 0:
        final_list.append(num)
else:
    final_list.sort()
    print(final_list)
    length = len(final_list)
    while final_list:
        num = final_list.pop()
        print(f" {length - len(final_list)} => {num}")
    else:
        print("All Numbers Printed")
# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"

# -------------- 2 --------------- #
print("-" * 50)

ran = range(20)

for i in ran:


    i += 1
    if i == 6 or i == 8 or i == 12:
        continue
    print(f"{i}".zfill(2))
else:
    print("All Numbers Printed")

# -------------- 3 --------------- #
print("-" * 50)

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

for rank, value in my_ranks.items():
    value = 100 if value == 'A' else 80 if value == 'B' else 40
    print(f"My Rank in {rank} Is A And This Equal {value} Points")

# -------------- 4 --------------- #
print("-" * 50)

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

for name, value in students.items():
    print("------------------------------")
    print(f"-- Student Name => {name}")
    print("------------------------------")
    for rank, level in value.items():
        level = 100 if level == 'A' else 80 if level == 'B' else 40 if level == 'C' else 20
        print(f"{rank} => {level} Points")