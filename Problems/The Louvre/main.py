class Painting:
    museum = "Louvre"

    def __init__(self, title, year, painter):
        self.title = title
        self.year = year
        self.painter = painter

    def print(self):
        print(f'"{title}" by {artist} ({year}) hangs in the {self.museum}.')


title = input()
artist = input()
year = input()

bild = Painting(title, year, artist)
bild.print()
