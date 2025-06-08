#pragma once
#include "IPercentileCalculator.hpp"

class LinInterpolationPC : public IPercentileCalculator {
    public:
        LinInterpolationPC() = default;

        ~LinInterpolationPC() = default;

        int calculatePercentile(double percentile, const std::vector<int>& numbers) override;
};