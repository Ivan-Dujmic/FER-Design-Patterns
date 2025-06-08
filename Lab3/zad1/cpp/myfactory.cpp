#include "myfactory.hpp"

MyFactory& MyFactory::instance() {
    static MyFactory factory;
    return factory;
}