#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = ["Labrador", "Poodle", "German Shepherd", "Bulldog", "Golden Retriever", "Pug"]

    def __init__(self, name=None, breed=None):
        self._name = ""
        self._breed = ""
        if name is not None:
            self.set_name(name)
        if breed is not None:
            self.set_breed(breed)

    def set_name(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name

    def set_breed(self, breed):
        if breed not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed

#pass
