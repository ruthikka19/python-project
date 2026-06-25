numbers=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    print("enter element:",end="")
    num=int(input())
    numbers.append(num)

unique=[]

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates/unique elements:",unique)