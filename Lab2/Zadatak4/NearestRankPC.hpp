#pragma once
#include "IPercentileCalculator.hpp"

class NearestRankPC : public IPercentileCalculator {
    public:
        NearestRankPC() = default;

        ~NearestRankPC() = default;
        
        int calculatePercentile(double percentile, const std::vector<int>& numbers) override;
};