#include "animal.hpp"
#include "myfactory.hpp"

#include <string>

class Parrot : public Animal {
    private:
        std::string animal_name;
        static int reg;

    public:
        Parrot(const std::string& animal_name) : animal_name(animal_name) {}
        const char* name() override { return animal_name.c_str(); }
        const char* greet() override { return "Sto mu gromova!"; }
        const char* menu() override { return "brazilske orahe"; }
        static std::unique_ptr<Animal> create(const std::string& arg) {
            return std::make_unique<Parrot>(arg);
        }
};

int Parrot::reg = MyFactory::instance().registerCreator<Animal>("parrot", Parrot::create);