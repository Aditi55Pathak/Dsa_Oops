class A:
    _a = 10  # Protected
    __b = 20  # Private

    def show(self):
        print("Acessing A inside class : ", self._a)
        print("Acessing B inside class : ", self.__b)

obj1=A()
obj1.show()         
print("Accessing outside the class : ",obj1._a)
# print("Accessing outside the class : ",obj1.__b) error