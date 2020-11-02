times = int(input())
result = []

for _ in range(times):
    x = int(input())
    if x % 7 == 0:
        result.append(x * x)

for y in result:
    print(y)
