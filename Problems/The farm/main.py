money = int(input())

price_sheep = 6769
price_cow = 3848
price_pig = 1296
price_goat = 678
price_chicken = 23

if money >= price_sheep:
    print(money // price_sheep, "sheep")

elif money >= price_cow:
    if money // price_cow > 1:
        print(money // price_cow, "cows")
    else:
        print(money // price_cow, "cow")

elif money >= price_pig:
    if money // price_pig > 1:
        print(money // price_pig, "pigs")
    else:
        print(money // price_pig, "pig")

elif money >= price_goat:
    if money // price_goat > 1:
        print(money // price_goat, "goats")
    else:
        print(money // price_goat, "goat")

elif money >= price_chicken:
    if money // price_chicken > 1:
        print(money // price_chicken, "chickens")
    else:
        print(money // price_chicken, "chicken")

else:
    print('None')
