# Write a program which creates a class called suspect.
# The class should have the attributes title, name and location.
# Create three objects player1, player2 and player3 each of which uses characters and locations from Cluedo.
# Define methods called who_are_you and where_are_you
# When a suspect object calls each of these methods, the output could look like these…..

class suspect:
    # initialisation method
    def __init__(self, title, name, location):
        self.title = title
        self.name = name
        self.location = location

    def display_all_details(self):
        print("I am", self.name)
        print(self.title, "is in the", self.location)


# create 4 instances of car (i.e 4 OBJECTS)

player1 = suspect("Miss", "Scarlet", "Living room")
player2 = suspect("Mr", "Hubert", "Kitchen")
player3 = suspect("Rev", "Green", "Hall")

# call the display_all_details method for each object
player1.display_all_details()
player2.display_all_details()
player3.display_all_details()