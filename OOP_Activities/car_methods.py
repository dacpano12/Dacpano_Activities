class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.km_driven = 0

    # Method 1: Drive with validation
    def drive(self, km):
        if km < 0:
            print("❌ Distance cannot be negative!")
            return
        self.km_driven += km
        print(f"Drove {km} km. Total: {self.km_driven} km")

    # Method 2: Calculate car's age
    def age(self, current_year):
        return current_year - self.year

    # Method 3: String representation
    def __str__(self):
        return f"{self.year} {self.brand} {self.model} — {self.km_driven} km"


# Test
my_car = Car("Toyota", "Vios", 2020)
my_car.drive(50)
my_car.drive(30)
my_car.drive(-5)  # Error message
print(f"Age in 2026: {my_car.age(2026)} years")
print(my_car)
