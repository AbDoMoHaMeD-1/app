from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

# Subclass implementing the abstract methods
class Dog(Animal):
    
    def sound(self):
        return "Bark"
    
    def move(self):
        return "Runs"

# Another subclass implementing the abstract methods
class Bird(Animal):
    
    def sound(self):
        return "Chirp"
    
    def move(self):
        return "Flies"

# Instantiate objects of subclasses
dog = Dog()
bird = Bird()

# Call implemented methods
print(f"Dog sound: {dog.sound()}")
print(f"Dog movement: {dog.move()}")
print(f"Bird sound: {bird.sound()}")
print(f"Bird movement: {bird.move()}")
