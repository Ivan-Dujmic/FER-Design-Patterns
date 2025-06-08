#pragma once
#include <vector>

class IAction {
    public:
        virtual ~IAction() = default;

        virtual void execute(const std::vector<int>& collection) = 0;
};