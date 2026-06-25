numbers=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    print("enter element:",end="")
    num=int(input())
    numbers.append(num)

for i in range(n):
    for j in range(i+1,n):
        if numbers[i]>numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]

print("Sorted list:",numbers)