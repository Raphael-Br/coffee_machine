class Sphere:
    PI = 3.1415

    def __init__(self, r):
        self.radius = r
        self.volume = (4 / 3) * self.PI * (self.radius ** 3)


# obj = Sphere(3)
# print(obj.volume)
