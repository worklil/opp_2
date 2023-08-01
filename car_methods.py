class car:
    # initialisation method
    def __init__(self, registration, colour, make, model):
        self.registration = registration
        self.colour = colour
        self.make = make
        self.model = model

# create 4 instances of car (i.e 4 OBJECTS)

car1 = car("AB01CDE", "White", "Ford", "Focus")
car2 = car("FG02HIJ", "Blue", "Vauxhall", "Corsa")
car3 = car("KL03MNO", "Green", "Volkswagen", "Polo")
car4 = car("PQ04RST", "Red", "Toyota", "Yaris")

# access some or all of the attributes of the objects
print("The first car is made by", car.make)
print("The second car is", car2.colour)
print("The third car is a", car3.make, car3.model)
print("The fourth car has Reg No", car4.registration)
print()
print(car1.colour, car1.make, car1.model, "with Reg No", car1.registration)
print(car2.colour, car2.make, car2.model, "with Reg No", car2.registration)
print(car3.colour, car3.make, car3.model, "with Reg No", car3.registration)
print(car4.colour, car4.make, car4.model, "with Reg No", car4.registration)