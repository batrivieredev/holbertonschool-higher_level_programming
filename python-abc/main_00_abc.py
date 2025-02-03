#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())  # Output: Bark
print(garfield.sound())  # Output: Meow

# Uncommenting the following line will raise a TypeError because Animal is abstract
# animal = Animal()
# print(animal.sound())
