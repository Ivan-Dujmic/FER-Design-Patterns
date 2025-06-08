#pragma once
#include "IIntegerGenerator.hpp"

class NormalDistIG : public IIntegerGenerator {
    private:
        int mean;
        int stddev;
        int count;
        
    public:
        NormalDistIG(int mean, int stddev, int count);

        ~NormalDistIG() = default;
        
        std::vector<int> generateIntegers() override;
};