def main():
    output_file = open("name.txt", 'w')
    name = input("Please enter name: ")
    print(name, file=output_file)
    output_file.close()

    input_file = open("name.txt", 'r')
    name = input_file.read().strip()
    input_file.close()
    print("your name is", name)

    number_in_file = open("numbers.txt", "r")
    num_one = int(number_in_file.readline())
    num_two = int(number_in_file.readline())
    number_in_file.close()
    print(num_two + num_one)

    number_in_file = open("numbers.txt", "r")
    total = 0
    for line in number_in_file:
        number = int(line)
        total += number
    number_in_file.close()
    print("total : ", total)


main()
