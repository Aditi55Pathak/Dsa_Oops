class Icecream:

    # Default Constructor
    def __init__(self):
        print("Hey! It's me")

    # Parameterized Construtor
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price
        print(f"Taking infos about Icecream : {flavor},{price}")


i = Icecream("Vanilla", 90)
print(i)

