"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

    when the wrong information is trying to be stored

2. When will a ZeroDivisionError occur?

        When it tries to divide by 0?

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

        dunno, tried to make it ask the question again if a 0 is given but that failed lol

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
