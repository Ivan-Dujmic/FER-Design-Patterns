#pragma once
#include "IAction.hpp"

class SumAction : public IAction {
    public:
        SumAction() = default;
        
        ~SumAction() = default;

        void execute(const std::vector<int>& collection) override;
};