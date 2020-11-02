a = int(input())
b = int(input())
numbers = []

for i in range(a, b + 1, 1):
    if i % 3 == 0:
        numbers.append(i)

summe = 0
for nr in numbers:
    summe += nr

print(summe / len(numbers))
