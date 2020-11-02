cafes = []

while True:
    cafe = input().split()
    if cafe[0] == 'MEOW':
        break
    cafe[1] = int(cafe[1])
    cafes.append(cafe)

max_guests = cafes[0][1]
max_cafe = cafes[0][0]

for x in range(len(cafes)):
    if cafes[x][1] > max_guests:
        max_guests = cafes[x][1]
        max_cafe = cafes[x][0]

print(max_cafe)

