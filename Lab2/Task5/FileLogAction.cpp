#include "FileLogAction.hpp"
#include <chrono>
#include <fstream>
#include <iomanip>
#include <ctime>
#include <stdexcept>

FileLogAction::FileLogAction(const std::string& filename) {
    fileStream.open(filename, std::ios::app); // Append mode
    if (!fileStream.is_open()) {
        throw std::runtime_error("Failed to open file: " + filename);
    }
}

FileLogAction::~FileLogAction() {
    if (fileStream.is_open()) {
        fileStream.close();
    }
}

void FileLogAction::execute(const std::vector<int>& collection) {
    if (fileStream.is_open()) {
        auto now = std::chrono::system_clock::now();
        auto time = std::chrono::system_clock::to_time_t(now);
        std::tm* localTime = std::localtime(&time);
        fileStream << std::put_time(localTime, "%Y-%m-%d %H:%M:%S") << " ; Numbers: ";
        for (const auto& number : collection) {
            fileStream << number << " ";
        }
        fileStream << std::endl;
    } else {
        throw std::runtime_error("File stream is not open.");
    }
}