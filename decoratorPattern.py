class Coffee:
    def cost(self):
        return 5


class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2


class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1


class WhipCreamDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 3


simple_coffee = Coffee()
print(f"Simple Coffee: ${simple_coffee.cost()}")

milk_coffee = MilkDecorator(simple_coffee)
print(f"Milk Coffee: ${milk_coffee.cost()}")

sweet_milk_coffee = SugarDecorator(milk_coffee)
print(f"Sweet Milk Coffee: ${sweet_milk_coffee.cost()}")

premium_coffee = WhipCreamDecorator(sweet_milk_coffee)
print(f"Premium Coffee: ${premium_coffee.cost()}")
