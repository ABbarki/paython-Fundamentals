numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("largest:", largest)
print("smallest:",smallest)