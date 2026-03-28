#include "animal.hpp"
#include "myfactory.hpp"

#include <string>

class Tiger : public Animal {
    private:
        std::string animal_name;
        static int reg;

    public:
        Tiger(const std::string& animal_name) : animal_name(animal_name) {}
        const char* name() override { return animal_name.c_str(); }
        const char* greet() override { return "Mijau"; }
        const char* menu() override { return "mlako mlijeko"; }
        static std::unique_ptr<Animal> create(const std::string& arg) {
            return std::make_unique<Tiger>(arg);
        }
};

int Tiger::reg = MyFactory::instance().registerCreator<Animal>("tiger", Tiger::create);