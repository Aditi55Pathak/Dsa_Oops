# Polymorphism

print(5 + 5)
print("5" + "5")
# Here function is only one print function but output types are different.

print(len("Aditi"))
print(len(["Aditi", "Aanya", "Rohit"]))
# Here function is only one len function but output types are different
# because in first it will consider all character, in second it will consider
# whole string as one character.


# Method Overloading


class A:
    def show(self):
        print("Hey! Good Morning")

    def show(self, firstname=""):
        print("My firstname is : ", firstname)

    def show(self, firstname="", lastname=""):
        print("My firstname is : ", firstname, " and lastname is : ", lastname)


obj1 = A()
obj1.show()
obj1.show("Aditi")
obj1.show("Aditi", "Pathak")


# Python does not support function overloading in
#  the traditional sense (as seen in languages like C++ or Java),
# where multiple functions with the same name can exist in the same
# scope but with different parameter lists. However, you can achieve
# similar functionality in Python using various techniques,
#  such as default parameter values, variable-length arguments, and function annotations


class A:
    def show(self, firstname="", lastname=""):
        if firstname and lastname:
            print("My firstname is:", firstname, "and lastname is:", lastname)
        elif firstname:
            print("My firstname is:", firstname)
        else:
            print("Hey! Good Morning")


obj1 = A()
obj1.show()  # Output: Hey! Good Morning
obj1.show("Aditi")  # Output: My firstname is: Aditi
obj1.show("Aditi", "Pathak")  # Output: My firstname is: Aditi and lastname is: Pathak


# Method Overriding.


class Car:
    def show(self):
        print("I am the parent class")


class Bicycle(Car):
    def show(self):
        print("I am the child class")


c = Car()
b = Bicycle()
b.show()
c.show()
