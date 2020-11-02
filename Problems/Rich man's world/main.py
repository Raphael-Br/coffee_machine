years = 0
interest = 1.071
deposit = int(input())

while deposit < 700000:
    deposit *= interest
    years += 1

print(years)
