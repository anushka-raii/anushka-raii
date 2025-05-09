class House:
    def __init__(self, owner, location, rent):
        self.owner = owner
        self.location = location
        self.rent = rent

    def increase_rent(self, amount):
        self.rent += amount

house1 = House("Ravi", "Pune", 15000)
house2 = House("Mira", "Delhi", 18000)


house2.increase_rent(2000)
print("Mira’s new rent:", house2.rent)

house1.location = "Mumbai"
print("Ravi’s new location:", house1.location)

del house2
print("House 2 deleted")
