#include "NearestRankPC.hpp"
#include <stdexcept>
#include <algorithm>

int NearestRankPC::calculatePercentile(double percentile, const std::vector<int>& numbers) {
    if (numbers.empty()) {
        throw std::invalid_argument("The numbers vector is empty.");
    }
    if (percentile < 0 || percentile > 100) {
        throw std::out_of_range("Percentile must be between 0 and 100.");
    }

    int index = (static_cast<int>(percentile * (numbers.size()) / 100.0 + 0.5)) - 1;
    
    std::vector<int> sortedNumbers = numbers;
    std::sort(sortedNumbers.begin(), sortedNumbers.end());
    return sortedNumbers[index];
}