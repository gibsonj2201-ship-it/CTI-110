# jason gibson
#10/5/2026
# P2HW2
# six module test grades and display summary

"""Collect six module test grades and display summary statistics."""

module_1_grade = float(input("Enter grade for Module 1: "))
module_2_grade = float(input("Enter grade for Module 2: "))
module_3_grade = float(input("Enter grade for Module 3: "))
module_4_grade = float(input("Enter grade for Module 4: "))
module_5_grade = float(input("Enter grade for Module 5: "))
module_6_grade = float(input("Enter grade for Module 6: "))

module_grades = [
    module_1_grade,
    module_2_grade,
    module_3_grade,
    module_4_grade,
    module_5_grade,
    module_6_grade,
]

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

print("------------Results------------")
print(f"{'Lowest Grade:':<25}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<25}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<25}{sum_of_grades:.1f}")
print(f"{'Average:':<25}{average_grade:.2f}")
print("----------------------------------------------")
