#pragma once
#include "IAction.hpp"

class AverageAction : public IAction {
    public:
        AverageAction() = default;
        
        ~AverageAction() = default;

        void execute(const std::vector<int>& collection) override;
};