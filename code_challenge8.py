print("MULTIPLICATION TABLE MAKER")

number = int(input("Enter a number: "))

print(f"\nMultiplication table for {number}:")

for d in range(1, 11):
    result = number * d
    print(f"{number} x {d} = {result}")
