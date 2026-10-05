# jason gibson
# 10/5/2026
# P2HW1
# Calculate and display a simple travel budget.


"""Calculate and display a simple travel budget."""


LABEL_WIDTH = 22
RULE = "-" * 35


def main():
    print("This program calculates and displays travel expenses")
    print()

    budget = float(input("Enter Budget: "))
    destination = input("Enter your travel destination: ")
    fuel = float(input("How much do you think you will spend on gas? "))
    accommodation = float(
        input("Approximately, how much will you need for accommodation/hotel? ")
    )
    food = float(input("Last, how much do you need for food? "))

    remaining_balance = budget - fuel - accommodation - food

    print()
    print("----------Travel Expenses----------")
    print(f"{'Location:':<{LABEL_WIDTH}}{destination}")
    print(f"{'Initial Budget:':<{LABEL_WIDTH}}${budget:.2f}")
    print(f"{'Fuel:':<{LABEL_WIDTH}}${fuel:.2f}")
    print(f"{'Accommodation:':<{LABEL_WIDTH}}${accommodation:.2f}")
    print(f"{'Food:':<{LABEL_WIDTH}}${food:.2f}")
    print(RULE)
    print()
    print(f"Remaining Balance: ${remaining_balance:.2f}")


if __name__ == "__main__":
    main()
