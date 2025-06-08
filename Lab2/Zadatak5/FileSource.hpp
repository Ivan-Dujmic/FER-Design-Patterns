#pragma once
#include "INumberSource.hpp"
#include <fstream>
#include <string>

class FileSource : public INumberSource {
    private:
        std::ifstream fileStream;

    public:
        FileSource(const std::string& filePath);

        ~FileSource() override;

        int getNumber() override;
};