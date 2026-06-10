import math

# Read comma-separated values
d_values = input("Enter values of D separated by commas: ").split(',')

result = []

for d in d_values:
    D = int(d)
    Q = int(math.sqrt((2 * 50 * D) / 30))
    result.append(str(Q))

print(",".join(result))