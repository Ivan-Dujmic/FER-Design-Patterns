#include "FileSource.hpp"
#include <stdexcept>

FileSource::FileSource(const std::string& filePath) {
    fileStream.open(filePath);
    if (!fileStream.is_open()) {
        throw std::runtime_error("Could not open file: " + filePath);
    }
}

FileSource::~FileSource() {
    if (fileStream.is_open()) {
        fileStream.close();
    }
}

int FileSource::getNumber() {
    int number;
    if (fileStream >> number) {
        if (number >= 0 || number == -1) {
            return number;
        } else {
            throw std::runtime_error("Negative (non -1) number in file: " + std::to_string(number));
        }
    } else {
        if (fileStream.eof()) {
            return -1;
        } else {
            throw std::runtime_error("Failed to read an integer from file.");
        }
    }
}