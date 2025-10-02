# Student Grades Tracker
# Ask the user for student names and their grades (loop until "done").
# Store them in a dictionary: {name: grade}.
# Print:
# Class average
# Highest grade + student
# Lowest grade + student
grades = {}

while True:

    student_name = input("What's the name? ")

    if student_name.lower() == "done":
        break

    student_grade = float(input("What's the grade? "))

    if student_grade > 20 or student_grade < 0:
        print("the grades should be between 0-20 , please try again! ")
        continue
    else:
        grades.update({student_name: student_grade})





if grades:  # only run if we have at least 1 student
    class_avg = sum(grades.values()) / len(grades)

    highest_student = max(grades, key=grades.get)
    lowest_student = min(grades, key=grades.get)

    print("===== Grades Summary =====")
    print(f"Class average is: {class_avg:.2f}")
    print(f"Highest grade is: {grades[highest_student]} (belongs to {highest_student})")
    print(f"Lowest grade is: {grades[lowest_student]} (belongs to {lowest_student})")
    print()
else:
    print("No students were entered.")
