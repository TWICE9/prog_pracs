"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory",
               "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)
max_length = 3
# print(*STATE_NAMES, sep="\n".rjust(3))

for x, y in STATE_NAMES.items():
    print("{:{}} is {}".format(x, max_length, y))

state = input("\nEnter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("\nEnter short state: ").upper()
