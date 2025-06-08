#pragma once
#include "IIntegerGenerator.hpp"

class FibIG : public IIntegerGenerator {
    private:
        int count;

    public:
        FibIG(int count);

        ~FibIG() = default;

        std::vector<int> generateIntegers() override;
};