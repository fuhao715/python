# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-1-22
# * Time: 上午9:22
# * To change this template use File | Settings | File Templates.
""" Implementation of the abstract factory pattern """
import random

class PetShop:
    """ A pet shop """

    def __init__(self, animal_factory=None):
        """
        pet_factory is our abstract factory.
        We can set it at will.
        """
        self.pet_factory = animal_factory

    def show_pet(self):
        """
        Creates and shows a pet using the abstract factory
        """
        pet = self.pet_factory.get_pet()

        print("this is a lovely ", pet)
        print("It says ", pet.speak())
        print("It eats ", self.pet_factory.get_food())



# Stuff that our factory makes
class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"

# create the proper family
def get_factory(name):
    """
    let's be dynamic!
    """
    #random.choice([DogFactory, CatFactory])()
    return eval(name+'Factory()')

# Show pets with various factories
if __name__ == "__main__":
    shop = PetShop()
    shop.pet_factory = get_factory("Dog")
    shop.show_pet()
    print("=" * 20)
    shop.pet_factory = get_factory("Cat")
    shop.show_pet()
    print("=" * 20)
