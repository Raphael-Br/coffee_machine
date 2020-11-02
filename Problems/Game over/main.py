scores = input().split()
correct = 0
incorrect = 0

for x in scores:
    if x == 'C':
        correct += 1
    elif x == 'I':
        incorrect += 1
    if incorrect >= 3:
        break

if incorrect >= 3:
    print("Game over")
else:
    print("You won")

print(correct)
