#!/usr/bin/env python3

approved_breeds = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei", 
    "Beagle", "French Bulldog", "Pug", "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Mastiff"):
        # Use the property setters (not the protected attributes)
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Check that name is a string between 1 and 25 characters.
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        # Check that breed is in the list of approved breeds.
        if value in approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
