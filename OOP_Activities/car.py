class Car:
    # Class attribute — shared by all cars
    wheels = 4

    def __init__(self, brand, model, year):
        # Instance attributes — unique to each car
        self.brand = brand
        self.model = model
        self.year = year


# Create 3 Car objects
car1 = Car("Toyota", "Vios", 2023)
car2 = Car("Honda", "Civic", 2022)
car3 = Car("Ford", "Everest", 2024)

# Display
print(f"Car 1: {car1.year} {car1.brand} {car1.model} — Wheels: {car1.wheels}")
print(f"Car 2: {car2.year} {car2.brand} {car2.model} — Wheels: {car2.wheels}")
print(f"Car 3: {car3.year} {car3.brand} {car3.model} — Wheels: {car3.wheels}")
