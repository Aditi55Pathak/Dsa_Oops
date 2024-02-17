# A class which contains one or more abstract class    ----> Abstract Class
# A method that have declaration but does not hae implementation  ----> Abstract Method

from abc import ABC, abstractmethod


class Vehical(ABC):
    @abstractmethod
    def specifications(self):
        pass


class Car(Vehical):

    def start(self):
        print("Starting a car")

    def specifications(self):
        print("I am a parent Vehical")
    


class Motercycle(Car):

    def brake(self):
        print("Here we had a break")


# veh = Vehical()  ---> can't initiate

car = Car()
car.start()
