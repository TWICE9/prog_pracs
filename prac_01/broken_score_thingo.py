"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!

def main():
    score_one = int(input("enter your score: "))
    if score_one in range(50, 90):
        print("Passable.")
    elif score_one in range(90, 101):
        print("Excellent!")
    elif score_one < 50:
        print("Bad.")
    else:
        print("Invalid score...")


main()
