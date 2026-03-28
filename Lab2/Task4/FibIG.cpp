#include "FibIG.hpp"

FibIG::FibIG(int count) : count(count) {}

std::vector<int> FibIG::generateIntegers() {
    std::vector<int> numbers;
    int a = 0, b = 1;
    for (int i = 0 ; i < count ; i++) {
        numbers.push_back(a);
        int next = a + b;
        a = b;
        b = next;
    }
    return numbers;
}