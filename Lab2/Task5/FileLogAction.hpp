#pragma once
#include "IAction.hpp"
#include <fstream>

class FileLogAction : public IAction {
    private:
        std::ofstream fileStream;
    
    public:
        FileLogAction(const std::string& filename);

        ~FileLogAction() override;

        void execute(const std::vector<int>& collection) override;
};