#Pet Tracker

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def show_info(self):
        try:
            print(f"Pet Info: {self.name} is a {self.age}-year-old {self.species}.")
        except AttributeError:
            print(f"Pet Info: {self.name} is a {self.species}, but age info is missing.")

pet1 = Pet("Buddy", "Dog", 4)
pet2 = Pet("Luna", "Cat", 3)

pet1.show_info()
pet2.show_info()

del pet2.age
print("\nAfter deleting Luna's age:")
pet2.show_info()
