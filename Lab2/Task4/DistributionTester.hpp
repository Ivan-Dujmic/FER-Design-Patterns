#pragma once
#include "IIntegerGenerator.hpp"
#include "IPercentileCalculator.hpp"
#include <vector>

class DistributionTester {
    private:
        IIntegerGenerator* integerGenerator;
        IPercentileCalculator* percentileCalculator;
        std::vector<int> numbers;
        
    public:
        DistributionTester(IIntegerGenerator& ig, IPercentileCalculator& pc);

        ~DistributionTester() = default;

        void generateIntegers();
        
        int calculatePercentile(double percentile);

        std::vector<int> getNumbers() const;

        void setIntegerGenerator(IIntegerGenerator& ig);

        void setPercentileCalculator(IPercentileCalculator& pc);
};