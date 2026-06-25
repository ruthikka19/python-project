list1=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    print("enter element:",end="")
    num=int(input())
    list1.append(num)
list2=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    print("enter element:",end="")
    num=int(input())
    list2.append(num)


common=[]

for item in list1:
    if item in list2:
        common.append(item)

print("Common elements:",common)