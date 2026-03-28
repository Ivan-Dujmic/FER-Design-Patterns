#include "NormalDistIG.hpp"
#include <random>

NormalDistIG::NormalDistIG(int mean, int stddev, int count) : mean(mean), stddev(stddev), count(count) {}
        
std::vector<int> NormalDistIG::generateIntegers() {
    std::vector<int> numbers;
    std::default_random_engine generator;
    std::normal_distribution<double> distribution(mean, stddev);
    
    for (int i = 0 ; i < count ; i++) {
        numbers.push_back(static_cast<int>(distribution(generator)));
    }
    
    return numbers;
}