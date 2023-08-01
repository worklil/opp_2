class car:
    # initialisation method
    def __init__(self, registration, colour, make, model):
        self.registration = registration
        self.colour = colour
        self.make = make
        self.model = model
    # method to display all ditails of the car object
    def display_all_details(self):
        print(self.colour, self.make, self.model, "with Reg No", self.registration)

# create 4 instances of car (i.e 4 OBJECTS)

car1 = car("AB01CDE", "White", "Ford", "Focus")
car2 = car("FG02HIJ", "Blue", "Vauxhall", "Corsa")
car3 = car("KL03MNO", "Green", "Volkswagen", "Polo")
car4 = car("PQ04RST", "Red", "Toyota", "Yaris")

# call the display_all_details method for each object
car1.display_all_details()
car2.display_all_details()
car3.display_all_details()
car4.display_all_details()
