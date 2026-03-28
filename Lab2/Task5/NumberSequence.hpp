#pragma once
#include "INumberSource.hpp"
#include "IAction.hpp"

class NumberSequence {
    private:
        INumberSource* numberSource;
        std::vector<int> collection;
        std::vector<IAction*> actions;

    public:
        NumberSequence(INumberSource* numberSource);

        ~NumberSequence() = default;    // We consider the source and actions to be managed externally

        void attachAction(IAction* action);

        void detachAction(IAction* action);

        void changeSource(INumberSource* newSource);

        void start();
};