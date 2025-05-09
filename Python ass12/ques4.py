#Empty Car Class Placeholder

class Car:
    pass
class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def update_mileage(self, new_mileage):
        self.mileage = new_mileage

    def display(self):
        print("Car Info:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Mileage:", self.mileage)


car = Car("Toyota", "Fortuner", 12000)
car.update_mileage(15000)
car.display()
