def simple_interest(principal,rate,time):
    return (principal*rate*time)/100


def main():
    principal=float(input("Enter Principal Amount: "))
    rate=float(input("Enter Rate of Interest: "))
    time=float(input("Enter Time (Years): "))

    si=simple_interest(principal,rate,time)
    print(f"Simple Interest:{si}")


main()