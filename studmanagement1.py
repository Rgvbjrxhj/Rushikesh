def grade (marks):
    if marks<=100 and marks>80:
        grade="A"
    elif marks<=80 and marks >60:
        grade = "B"
    elif marks<=60 and marks >40:
        grade ="C"
    else:
        grade ="F"

def ADD (students):
    name = input("Enter student name:")
    age = int(input("Enter student age"))
    marks = int(input("Enter marks out of 100: "))
    if name in students:
        print("Updating student data")
        students[name]= {"age":age,"marks":marks,"Grade":grade(marks)}
    else:
        students={"Name":name,"Age":age,"Marks":marks,"Grade":grade(marks)}


def display(students):
    print(students)


students={}
while True:
    c=input("1.Add or Update student info\n2.Display student information\n3.exit\nEnter your choice: ")
    if c==1:
        ADD(students)
    elif c==2:
        display(students)
    elif c==3:
        print("Exiting program")
        break
    else:
        print("Invalid option")

