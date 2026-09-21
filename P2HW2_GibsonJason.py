# Jason Gibson
# 9/21/2026
# P2HW2
# budget and expense calculator

# Ask the user for their budget
budget = float(input("Enter your budget: $"))

# Ask for travel destination
destination = input("Enter your travel destination: ")

# Ask for expenses
gas = float(input("Enter the amount you will spend on gas: $"))
accommodation = float(input("Enter the amount you will spend on accommodation: $"))
food = float(input("Enter the amount you will spend on food: $"))

# Add expenses
total_expenses = gas + accommodation + food

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("\nTravel Summary")
print("Destination:", destination)
print(f"Total expenses: ${total_expenses:.2f}")
print(f"Remaining budget: ${remaining_budget:.2f}")