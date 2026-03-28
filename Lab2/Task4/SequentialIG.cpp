#include "SequentialIG.hpp"

SequentialIG::SequentialIG(int start, int end, int step) : start(start), end(end), step(step) {}

std::vector<int> SequentialIG::generateIntegers() {
    std::vector<int> numbers;
    for (int i = start ; i <= end ; i += step) {
        numbers.push_back(i);
    }
    return numbers;
}