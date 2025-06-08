#pragma once
#include <vector>

class IIntegerGenerator {
    public:
        virtual ~IIntegerGenerator() = default;
        virtual std::vector<int> generateIntegers() = 0;
};