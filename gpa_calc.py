"""
Grade Point Average Calculator App
A program that calculates student GPAs, simulates grade scenarios, and provides
grade requirements for target averages.

Author: Sergio Figueroa
Date: May 2025
"""

# Initialize application and collect user information
# -------------------------------------------------
print("Welcome to my Grade Point Average (GPA) Calculator App !")
user_name = (input("What is your name ").title())

# Grade collection with input validation
# ------------------------------------
# Ensure valid positive integer input for number of grades
while True:
    try:
        grades_num = int(input("How many grades would you like to enter: "))
        if grades_num <= 0:
            print("Please enter a positive number")
            continue
        break
    except ValueError:
        print("Please enter a valid integer")

# Initialize empty list for grade storage
grades_list = []

# Collect individual grades with float validation
for i in range(0, grades_num):
    grade = float(input("Enter grade: "))
    grades_list.append(grade)


# Grade processing and statistical calculations
# ------------------------------------------
# Sort grades in descending order for display
hilo_grades = sorted(grades_list, reverse=True)
print("\nGrades highest to lowest: ")
for grades in hilo_grades:
    print(grades)

# Calculate current average with 2 decimal precision
real_avg = sum(grades_list)/len(grades_list)
real_avg= round(real_avg, 2)

# Display comprehensive grade summary
print(f"\n{user_name}'s Grade Summary:")
print(f"\tTotal number of grades: {grades_num}")
print(f"\tHighest grade {max(grades_list)}")
print(f"\tLowest grade {min(grades_list)}")
print(f"\tAverage: {real_avg}")

# Target grade calculation
# ----------------------
# Validate desired average input
while True:
    try:
        wanted_avg = float(input("What is your desired average: "))
        if wanted_avg <= 0:
            print("Please enter a positive number")
            continue
        break
    except ValueError:
        print("Please enter a valid float")

# Calculate required grade for desired average
req_grade = wanted_avg*(len(grades_list)+1) - sum(grades_list)
req_grade = round(req_grade, 2)

print(f"\nGood luck {user_name}!")
print(f"You will need to get a {req_grade} on your next assignment to earn a {wanted_avg} average")
print("\nLets see what your average could have been if you did better/worse on an assignment.")

# Grade modification simulation
# ---------------------------
# Create deep copy of original grades for simulation
fake_grades = grades_list[:]

# Modify grades based on user input
grade_to_change = int(input("What grade would you like to change: "))
fake_grades.remove(grade_to_change)
new_grade = int(input(f"what would you like to change {grade_to_change} to: "))
fake_grades.append(new_grade)


# Calculate and display modified grade statistics

hilo_fk_grades = sorted(fake_grades, reverse=True)
print("\nNew Grades highest to lowest: ")
for grades in hilo_fk_grades:
    print(grades)

fake_avg = sum(fake_grades)/len(fake_grades)
fake_avg = round(fake_avg, 2)

# - Display fake grade summary
print(f"\n{user_name}'s New Grade Summary:")
print(f"\tTotal number of grades: {grades_num}")
print(f"\tHighest grade {max(fake_grades)}")
print(f"\tLowest grade {min(fake_grades)}")
print(f"\tAvarege: {fake_avg}")

# - Compare with original
print(f"\nYour new average would be {fake_avg} compared to your real average of {real_avg}!")
print(f"That is a change of {fake_avg - real_avg} points!")
print("Thank you for testing my app! Here is a Tank as a Reward!!")

# Final summary and ASCII art
 
print("      _______")
print("     |       |")
print("     |        |_______________________") 
print("     |        ________________________O") 
print("  ___|_______|___")
print(" |               |")
print(" |_______________|")
print(" |_______________|")
print("    O        O")
