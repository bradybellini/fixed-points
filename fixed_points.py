# Brady Bellini 
# I certify this is my own work

import random

def fixed_points():
    count = 0
    original_deck = [i for i in range(1,26)]
    draw1 = random.sample(range(1,26),25)
    draw2 = random.sample(range(1,26),25)

    print(f"Original Deck: \n{original_deck}\n")
    print(f"Draw 1: \n{draw1}\n")
    print(f"Draw 2: \n{draw2}\n")

    for i in range(len(draw1)):
        if draw1[i] == draw2[i]:
            count+= 1
    print(f"There are {count} fixed points.")

if __name__ == "__main__":
    fixed_points()
