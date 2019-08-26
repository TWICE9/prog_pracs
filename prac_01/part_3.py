def main():
    total = 0
    num_of_items = int(input("Number of Items: "))
    while num_of_items <= 0:
        print("Invalid number.\n")
        num_of_items = int(input("Number of Items: "))

    for i in range(num_of_items):
        price_of_item = float(input("Price of item: "))
        total += price_of_item
    if total > 100:
        discount = total * 0.1
        final_price = total - discount

    print("Total: $ {:.2f}".format(final_price), "number of items:", num_of_items)


main()
