#include "DistributionTester.hpp"

DistributionTester::DistributionTester(IIntegerGenerator& ig, IPercentileCalculator& pc) : integerGenerator(&ig), percentileCalculator(&pc) {}

void DistributionTester::generateIntegers() {
    numbers = integerGenerator->generateIntegers();
}

int DistributionTester::calculatePercentile(double percentile) {
    return percentileCalculator->calculatePercentile(percentile, numbers);
}

std::vector<int> DistributionTester::getNumbers() const {
    return numbers;
}

void DistributionTester::setIntegerGenerator(IIntegerGenerator& ig) {
    integerGenerator = &ig;
}

void DistributionTester::setPercentileCalculator(IPercentileCalculator& pc) {
    percentileCalculator = &pc;
}