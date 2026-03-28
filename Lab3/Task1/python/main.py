import os
from importlib import import_module

def myfactory(module_name):
    # Dynamically import the module and get the class from it
    return getattr(import_module('plugins.' + module_name), module_name)

def printGreeting(pet):
    print(f"{pet.name()} pozdravlja: {pet.greet()}")

def printMenu(pet):
    print(f"{pet.name()} voli {pet.menu()}.")

def main():
    pets = []
    for mymodule in os.listdir('plugins'):
        module_name, module_ext = os.path.splitext(mymodule)
        if module_ext == '.py':
            pet = myfactory(module_name)(f"Ljubimac {len(pets)}")
            pets.append(pet)

    for pet in pets:
        printGreeting(pet)
        printMenu(pet)

if __name__ == '__main__':
    main()