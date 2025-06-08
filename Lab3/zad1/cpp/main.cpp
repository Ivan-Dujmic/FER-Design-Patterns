#include "animal.hpp"
#include "myfactory.hpp"

#include <iostream>

void printGreeting(Animal& animal) {
    std::cout << animal.name() << " pozdravlja: " << animal.greet() << '\n';
}

void printMenu(Animal& animal) {
    std::cout << animal.name() << " voli " << animal.menu() << '\n';
}

int main() {
    auto& factory = MyFactory::instance();
    auto ids = factory.getIds<Animal>();
    for (const std::string& id : ids) {
        std::string pet = "Ljubimac " + id;
        auto animal = factory.create<Animal>(id, pet);
        if (animal) {
            printGreeting(*animal);
            printMenu(*animal);
        }
    }

    return 0;
}