#pragma once
#include "IAction.hpp"

class MedianAction : public IAction {
    public:
        MedianAction() = default;
        
        ~MedianAction() = default;

        void execute(const std::vector<int>& collection) override;
};