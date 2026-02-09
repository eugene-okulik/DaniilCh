class Flower:
    def __init__(self, name, color, stem_length, price, lifetime):
        self.name = name  # Название
        self.color = color  # Цвет
        self.stem_length = stem_length  # Длина
        self.price = price  # Цена
        self.lifetime = lifetime  # Время жизни

    def __repr__(self):
        return (
            f"{self.name} ({self.color}), "
            f"{self.stem_length}см, {self.price}р, {self.lifetime}дн"
        )


class Rose(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Архидея", color, stem_length, price, lifetime=7)


class Tulip(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Гладиолуз", color, stem_length, price, lifetime=5)


class Lily(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Лилия", color, stem_length, price, lifetime=10)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers  # список объектов Flower

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifetime(self):
        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_lifetime(self):
        self.flowers.sort(key=lambda flower: flower.lifetime)

    def find_by_lifetime(self, min_lifetime):
        return [
            flower for flower in self.flowers
            if flower.lifetime >= min_lifetime
        ]

    def show(self):
        for flower in self.flowers:
            print(flower)


rose1 = Rose("красный", 60, 300)
rose2 = Rose("белый", 55, 280)
tulip = Tulip("желтый", 40, 150)
lily = Lily("белый", 70, 400)

bouquet = Bouquet([rose1, rose2, tulip, lily])

print("Букет:")
bouquet.show()

print("\nСтоимость букета:", bouquet.total_price())
print("Среднее время жизни:", bouquet.average_lifetime())

print("\nСортировка по цене:")
bouquet.sort_by_price()
bouquet.show()

print("\nЦветы с жизнью от 7 дней:")
long_living = bouquet.find_by_lifetime(7)
for flower in long_living:
    print(flower)
