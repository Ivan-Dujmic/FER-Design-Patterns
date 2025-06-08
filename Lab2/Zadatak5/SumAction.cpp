#include "SumAction.hpp"
#include <iostream>

void SumAction::execute(const std::vector<int>& collection) {
    int sum = 0;
    for (int number : collection) {
        sum += number;
    }
    std::cout << "Sum: " << sum << std::endl;
}