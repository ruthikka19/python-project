def write_marks(filename):
    students=[]
    n=int(input("Enter no of students: "))
    for i in range(n):
        name=input("Enter student name: ")
        marks=input("Enter the marks: ")
        students.append(f"{name}:{marks}\n")

    with open(filename,"w") as f:
        f.writelines(students)
    print("Marks entered\n")



def read_marks(filename):
    print("Student Marks")
    with open(filename,"r") as f:
        for line in f:
            name,marks=line.strip().split(":")
            print(f"Student:{name},Marks:{marks}")


def append_marks(filename):
    name=input("Enter new student name: ")
    marks=input("Enter marks: ")
    with open(filename,"a") as f:
        f.write(f"{name}:{marks}\n")
    print("Student added\n")


def main():
    filename="student_marks.txt"
    write_marks(filename)
    read_marks(filename)
    append_marks(filename)
    print("\nAfter appending:")
    read_marks(filename)


main()