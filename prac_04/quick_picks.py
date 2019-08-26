import random

minimum = 1
maximum = 45
max_numbers = 6


def main():
    number_of_picks = int(input("how many picks?: "))
    for i in range(number_of_picks):
        quick_pick = []
        for j in range(max_numbers):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
