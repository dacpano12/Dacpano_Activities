class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome to OOP in Python.")

g = Greeter("Student")
g.greet()
