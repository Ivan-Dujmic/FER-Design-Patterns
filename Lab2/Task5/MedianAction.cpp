#include "MedianAction.hpp"
#include <iostream>
#include <algorithm>

void MedianAction::execute(const std::vector<int>& collection) {
    if (collection.empty()) {
        std::cout << "No numbers to calculate median." << std::endl;
        return;
    }

    std::vector<int> sorted = collection;
    std::sort(sorted.begin(), sorted.end());

    double median;
    size_t size = sorted.size();
    if (size % 2 == 0) {
        median = (sorted[size / 2 - 1] + sorted[size / 2]) / 2.0;
    } else {
        median = sorted[size / 2];
    }

    std::cout << "Median: " << median << std::endl;
}