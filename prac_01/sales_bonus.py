def main():
    """
    Program to calculate and display a user's bonus based on sales.
    If sales are under $1,000, the user gets a 10% bonus.
    If sales are $1,000 or over, the bonus is 15%.
    """

    sales = float(input("Enter Sales: $"))
    while sales <= 0:
        print("invalid")
        sales = float(input("Enter Sales: $"))
    if sales < 1000:
        bonus_calc = sales * 0.1
    else:
        bonus_calc = sales * 0.15

    print("Sale made $", sales, "Bonus from sale $", bonus_calc)


main()
