class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.km_driven = 0  # Track total distance driven

    # Method 1: Drive — add distance with validation
    def drive(self, km):
        if km < 0:
            print("❌ Distance cannot be negative!")
            return
        self.km_driven += km
        print(f"✅ Drove {km} km. Total: {self.km_driven} km")

    # Method 2: Calculate car's age
    def age(self, current_year):
        return current_year - self.year

    # Method 3: Friendly string representation
    def __str__(self):
        return f"{self.year} {self.brand} {self.model} — {self.km_driven} km driven"


# Test the Car class
print("=== Part 3: Car with Methods ===")
my_car = Car("Toyota", "Vios", 2020)

my_car.drive(50)
my_car.drive(30)
my_car.drive(-10)  # Should show error message

print(f"Car age in 2026: {my_car.age(2026)} years")
print(my_car)
