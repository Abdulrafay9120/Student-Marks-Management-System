print("===== Student Marks Management System =====")

name = input("Enter student name: ")

total = 0
count = 0

while True:

    subject = input("\nEnter subject name (or type 'done' to finish): ")

    if subject == "done":
        break

    marks = float(input("Enter marks out of 100: "))

    total = total + marks
    count = count + 1

if count > 0:

    average = total / count

    print("\n===== Student Report =====")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Subjects:", count)
    print("Average:", average, "%")

    if average >= 90:
        print("Grade: A+")

    elif average >= 80:
        print("Grade: A")

    elif average >= 70:
        print("Grade: B")

    elif average >= 60:
        print("Grade: C")

    else:
        print("Grade: Fail")

else:
    print("No subjects were entered.")

print("\nProgram Finished!")
