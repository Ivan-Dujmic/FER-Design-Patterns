#pragma once
#include "IIntegerGenerator.hpp"

class SequentialIG : public IIntegerGenerator {
    private:
        int start;
        int end;
        int step;

    public:
        SequentialIG(int start, int end, int step);

        ~SequentialIG() = default;

        std::vector<int> generateIntegers() override;
};