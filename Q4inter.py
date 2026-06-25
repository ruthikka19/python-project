numbers=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    print("enter element:",end="")
    num=int(input())
    numbers.append(num)

largest=numbers[0]
second=largest


for num in numbers:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num

print("Second largest number:",second)