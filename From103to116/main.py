# ------------------------------------- #
# ----- Assignment: From 106 to 116 --- #
# ------------------------------------- #
from abc import ABC, abstractmethod


class Game:
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):
        return float(self.price)


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

print()
# ------------------------------------------- #
print('=' * 50)


class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def full_details(self):
        if self.gender.lower() == "male":
            helloForm = "Mr"
        elif self.gender.lower() == "female":
            helloForm = "Miss"
        else:
            helloForm = ""
        if self.age < 40:
            to_be_40 = 40 - self.age
        elif self.age >= 40:
            to_be_40 = 0

        return f"Hello {helloForm} {self.first_name} {self.last_name.capitalize():1}. [{to_be_40}] Years to Reach 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40

# ------------------------------------------- #
print('=' * 50)


class Message:
    def __init__(self):
        pass

    @staticmethod
    def print_message():
        return "Hello From Class " + Message.__name__


print(Message.print_message())

# Output
# Hello From Class Message

# ------------------------------------------- #
print('=' * 50)


class Games:
    def __init__(self, games):
        self.games = games

    def show_games(self):
        if type(self.games) is str or (type(self.games) is list and len(self.games) == 1):
            print(f"I Have One Game Called \"{self.games}\"")
        elif type(self.games) is list:
            print("I Have Many Games:")
            for game in self.games:
                print(f"-- {game}")
        else:
            print(f"I Have {self.games} Games:")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.

# ------------------------------------------- #
print('=' * 50)


# Main Class
class Members:

    def __init__(self, n, p):
        self.name = n

        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"


# Create Admin Class Here
class Admins(Members):
    def __init__(self, name, permission):
        super().__init__(name, permission)


# Create Moderators Class Here
class Moderators(Members):
    pass


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator

# ------------------------------------------- #
print('=' * 50)

class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three

# Write The Class Called "Name" Here
class Name(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)
    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"

class Text(Name):
    pass

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero