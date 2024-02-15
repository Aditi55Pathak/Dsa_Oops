class A:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    @staticmethod # Decorator
    def hello():
        print("Hello")

    def getAdd(self):
        pass


s1=A(90,90)
s1.hello()