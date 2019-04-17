import random

def caps_word(word):
    word = str(word)
    word = word.capitalize()
    return word

def madLib():
    worst_food = input("What's your least favorite food? ")
    worst_food = caps_word(worst_food)

    index = random.randint(1,5)

    if index == 1:
        result = "It was the best of %s, it was the worst of %s" % (worst_food, worst_food)
    elif index == 2:
        result = ("Reach for the stars, for if you fall you'll land in the %s" % worst_food)
    elif index == 3:
        result =  ("Call me %s" % worst_food)
    else:
        result =  ("May the %s be with you" % worst_food)
    print(result)
    return result

madLib()

"""
if __name__ == '__main__':
    madLib()
"""


