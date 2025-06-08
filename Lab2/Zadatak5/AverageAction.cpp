#include "AverageAction.hpp"
#include <iostream>

void AverageAction::execute(const std::vector<int>& collection) {
    if (collection.empty()) {
        std::cout << "Average: 0" << std::endl;
        return;
    }

    int sum = 0;
    for (int number : collection) {
        sum += number;
    }
    double average = (double)sum / collection.size();
    
    std::cout << "Average: " << average << std::endl;
}