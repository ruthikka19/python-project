import csv
def write_employees(filename):
    employees=[]
    n=int(input("How many employees? "))
    for i in range(n):
        emp_id=input("Enter Employee ID: ")
        name=input("Enter Name: ")
        dept=input("Enter Department: ")
        salary=input("Enter Salary: ")
        employees.append([emp_id,name,dept,salary])

    with open(filename,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["EmpID", "Name", "Department", "Salary"])
        writer.writerows(employees)
    print("Employee records saved!\n")


def read_employees(filename):
    print("--- Employee Records ---")
    with open(filename,"r") as f:
        reader=csv.DictReader(f)
        for row in reader:
            print(f"ID: {row['EmpID']}|Name: {row['Name']}|Dept: {row['Department']}|Salary: {row['Salary']}")


def append_employee(filename):
    emp_id=input("Enter Employee ID: ")
    name=input("Enter Name: ")
    dept=input("Enter Department: ")
    salary=input("Enter Salary: ")

    with open(filename,"a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([emp_id,name,dept,salary])
    print("Employee added\n")

def main():
    filename="employees.csv"
    write_employees(filename)
    read_employees(filename)
    append_employee(filename)
    print("\nAfter appending:")
    read_employees(filename)

main()