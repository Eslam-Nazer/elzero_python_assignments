# ------------------------------------- #
# ----- Assignment: From 065 to 068 --- #
# ------------------------------------- #
import os
from pathlib import Path

index = 1
myFilePath = os.path.dirname(os.path.realpath(__file__)) + "/python"

# while index <= 50:
#     fileName = f"text-{index}.txt" if index != 25 else "special-text.txt"
#
#     file = open(f"{myFilePath}/{fileName}", "w")
#     if index != 25:
#         file.write(f"Elzero Web School => {fileName}\n")
#     index += 1

fileName = open(f"{myFilePath}/special-text.txt", "r")
print(os.path.dirname(__file__))
print(os.path.dirname(fileName.name))
print(os.path.basename(fileName.name))
folder_path = Path("./python")
folder_count = sum(1 for f in folder_path.iterdir() if f.is_file())
print(folder_count)

# ------------------------------------ #
print("-" * 50)

# file1 = open(f"{os.path.dirname(os.path.realpath(__file__))}/python/text-1.txt", "a")
# file1.write("Appended => Elzero Web School\n" * 50)
# file1.close()

# ------------------------------------ #
print("-" * 50)

# line_count = 0
# word_count = 0
# char_count = 0
# file = open(f"{os.path.dirname(os.path.realpath(__file__))}/python/text-1.txt", "r")
# for line in file:
#     line_count += 1
#     word_count += len(line.split())
#     char_count += len(line)
#
# file.seek(0)
# l_count = file.read().count("l")
#
# print(line_count)
# print(word_count)
# print(char_count)
# print(l_count)
#
# file.close()

# ------------------------------------ #
print("-" * 50)

# folder_path = "./python"
# files = [
#     f for f in os.listdir(folder_path)
#     if os.path.isfile(os.path.join(folder_path, f))
#     and f != "special-text.txt"
# ]
#
# files.sort(key=lambda x: int(x.split('-')[1].split('.')[0]), reverse=True)
#
# for f in files[:10]:
#     os.remove(os.path.join(folder_path, f))