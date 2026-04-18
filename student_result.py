# student_result_system

name = input("Enter Your Name :")

Mark1 = int(input("Enter marks of subject 1 :"))
Mark2 = int(input("Enter marks of subject 2 :"))
Marks3 = int(input("Enter marks of subject 3 :"))
Marks4 = int(input("Enter marks of subject 4 :"))

total = Mark1+Mark2+Marks3+Marks4
percentage = total/4

print("\nStudent Name :", name)
print("Total :", total)
print("Percentage :", percentage)

if percentage >= 80:
    print("Grade A+:")
elif percentage >= 70:
    print("Grade B ")
elif percentage > 60:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Fail")
