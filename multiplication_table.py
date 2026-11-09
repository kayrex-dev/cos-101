# Display a multiplication table from 1 to 12.
number = int(input("Enter a whole number: "))

print()
print(f"MULTIPLICATION TABLE FOR {number}")
print("==============================")

for multiplier in range(1, 13):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
