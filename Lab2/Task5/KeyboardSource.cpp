#include "KeyboardSource.hpp"
#include <iostream>
#include <limits>

int KeyboardSource::getNumber() {
    int number;

    while (true) {
        std::cout << "Enter a non-negative whole number (-1 to stop): ";
        std::cin >> number;
        if (std::cin.fail() || number < -1) {
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            std::cout << "Invalid input." << std::endl;
        } else break;
    }

    return number;
}