class Icecream:

    utensil = "Scoop"  # class attribute

    def __init__(self, flavor, price):
        self.flavor = flavor  # object attribute
        self.price = price
        print(f"Taking infos about Icecream --- Flavor is :{flavor},Price is :{price}")


i = Icecream("Vanilla", 90)
print(i)
print(i.flavor)

print(Icecream.utensil)
