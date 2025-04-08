# Base Class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power  # encapsulated (protected)
        self.origin = origin

    def introduce(self):
        print(f"Hi, I'm {self.name} from {self.origin}! 💥")

    def show_power(self):
        print(f"My power is: {self._power}")

# Subclass with inheritance and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, altitude_limit):
        super().__init__(name, power, origin)
        self.altitude_limit = altitude_limit

    def show_power(self):
        print(f"I can fly up to {self.altitude_limit} meters! ✈️")

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.gadgets = gadgets

    def show_power(self):
        print(f"I fight with gadgets: {', '.join(self.gadgets)} 🛠️")

# Example usage
ironman = TechHero("Ironman", "Genius-level intellect", "Earth", ["Repulsor", "Nano Suit"])
superman = FlyingHero("Superman", "Super strength", "Krypton", 10000)

ironman.introduce()
ironman.show_power()
print()
superman.introduce()
superman.show_power()


