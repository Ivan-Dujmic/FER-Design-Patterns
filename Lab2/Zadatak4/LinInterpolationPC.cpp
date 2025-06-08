#include "LinInterpolationPC.hpp"
#include <algorithm>
#include <stdexcept>

int LinInterpolationPC::calculatePercentile(double percentile, const std::vector<int>& numbers) {
    if (numbers.empty()) {
        throw std::invalid_argument("The input vector is empty.");
    }

    if (percentile < 0 || percentile > 100) {
        throw std::out_of_range("Percentile must be between 0 and 100.");
    }

    std::vector<int> sorted = numbers;
    std::sort(sorted.begin(), sorted.end());

    int N = sorted.size();

    // Edge cases
    double p_first = 100.0 * (1 - 0.5) / N;
    if (percentile < p_first) return sorted[0];
    double p_last = 100.0 * (N - 0.5) / N;
    if (percentile > p_last) return sorted[N - 1];

    double p_i = p_first;
    for (int i = 1 ; i < N ; i++) {
        double p_next = 100.0 * (i + 0.5) / N;

        if (percentile >= p_i && percentile <= p_next) {
            double interpolated = sorted[i-1] + N * (percentile - p_i) * (sorted[i] - sorted[i-1]) / 100.0;
            return static_cast<int>(interpolated + 0.5);    // Round to nearest integer
        }

        p_i = p_next;
    }

    return sorted[N - 1]; // This should not be reached
}