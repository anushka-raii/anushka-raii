# Vehicle → Car (Using super()

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_details(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def show_model(self):
        print(f"Model: {self.model}")


car1 = Car("Hyundai", 2020, "Creta")
car1.show_details()
car1.show_model()
