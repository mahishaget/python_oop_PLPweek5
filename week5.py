#Assignment 1
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power 
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and my power is {self._power}!")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

    def get_power(self):
        return self._power

    def set_power(self, new_power):
        self._power = new_power
class Speedster(Superhero):
    def use_power(self):
        print(f"{self.name} zooms past at lightning speed! ⚡")

class Flyer(Superhero):
    def use_power(self):
        print(f"{self.name} takes to the skies and flies! 🕊️")
hero1 = Speedster("Flashwave", "Super Speed", "Metroville")
hero2 = Flyer("Skyblaze", "Flight", "Cloud City")

hero1.introduce()
hero1.use_power()
hero2.introduce()
hero2.use_power()
#Activity 2
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water. ⛵")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

