#pragma once
#include <string>

class Animal {
    public:
        virtual ~Animal() {}
        virtual const char* name() = 0;
        virtual const char* greet() = 0;
        virtual const char* menu() = 0;
};