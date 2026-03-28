#include <iostream>

#include "DistributionTester.hpp"

#include "SequentialIG.hpp"
#include "NormalDistIG.hpp"
#include "FibIG.hpp"

#include "NearestRankPC.hpp"
#include "LinInterpolationPC.hpp"

int main() {
    SequentialIG seqIG = SequentialIG(5, 70, 7);
    NormalDistIG normIG = NormalDistIG(35, 20, 10);
    FibIG fibIG = FibIG(12);
    
    NearestRankPC nearPC = NearestRankPC();
    LinInterpolationPC linPC = LinInterpolationPC();
    
    DistributionTester tester = DistributionTester(seqIG, nearPC);
    tester.generateIntegers();
    std::cout << "\n----------------------------\n";
    for (int i : tester.getNumbers()) {
        std::cout << i << " ";
    }
    std::cout << "\nseqIQ + nearPC + p(30): " << tester.calculatePercentile(30) << '\n';
    tester.setPercentileCalculator(linPC);
    std::cout << "seqIQ + linPC + p(40): " << tester.calculatePercentile(40) << '\n';

    tester.setIntegerGenerator(normIG);
    tester.setPercentileCalculator(nearPC);
    tester.generateIntegers();
    std::cout << "----------------------------\n";
    for (int i : tester.getNumbers()) {
        std::cout << i << " ";
    }
    std::cout << "\nnormIQ + nearPC + p(50): " << tester.calculatePercentile(50) << '\n';
    tester.setPercentileCalculator(linPC);
    std::cout << "normIQ + linPC + p(60): " << tester.calculatePercentile(60) << '\n';

    tester.setIntegerGenerator(fibIG);
    tester.setPercentileCalculator(nearPC);
    tester.generateIntegers();
    std::cout << "----------------------------\n";
    for (int i : tester.getNumbers()) {
        std::cout << i << " ";
    }
    std::cout << "\nfibIQ + nearPC + p(70): " << tester.calculatePercentile(70) << '\n';
    tester.setPercentileCalculator(linPC);
    std::cout << "fibIQ + linPC + p(80): " << tester.calculatePercentile(80) << '\n';
    
    std::cout << "----------------------------\n";
    return 0;
}