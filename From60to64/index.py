# ------------------------------------- #
# ----- Assignment: From 060 to 064 --- #
# ------------------------------------- #

# ------------- 1 ---------------- #

def get_score(**skills):
    for skill, value in skills.items():
        print(f"{skill} => {value}")
    print('-' * 20)


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)

# ------------- 2 ---------------- #
print('-' * 50)


def get_people_scores(name=None, **skills):
    if name is not None:
        print(f"Hello {name} This Is Your Score Table:")
    for skill, value in skills.items():
        print(f"{skill} => {value}")
    print('-' * 20)


get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")

# ------------- 3 ---------------- #
print('-' * 50)

scores_list = {
    "Math": 90,
    "Science": 80,
    "Logic": 70,
}
def get_the_scores(name=None, **skills):
    if name is not None:
        print(f"Hello {name} This Is Your Score Table:")
        if len(skills) == 0:
            print("You don't have any skills")
        else:
            for skill, value in skills.items():
                print(f"{skill} => {value}")
        print('-' * 20)


get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)
