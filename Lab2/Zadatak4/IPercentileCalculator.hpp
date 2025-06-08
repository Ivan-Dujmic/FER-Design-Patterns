#pragma once
#include <vector>

class IPercentileCalculator {
    public:
        virtual ~IPercentileCalculator() = default;
        virtual int calculatePercentile(double percentile, const std::vector<int>& numbers) = 0;
};