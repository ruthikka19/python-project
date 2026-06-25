def ctof(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = ctof(celsius)
    print(f"Temperature in Fahrenheit: {fahrenheit}")

main()