#include "NumberSequence.hpp"
#include <chrono>
#include <thread>

NumberSequence::NumberSequence(INumberSource* numberSource) : numberSource(numberSource) {}

void NumberSequence::attachAction(IAction* action) {
    actions.push_back(action);
}

void NumberSequence::detachAction(IAction* action) {
    auto it = std::remove(actions.begin(), actions.end(), action);
    if (it != actions.end()) {
        actions.erase(it, actions.end());
    }
}

void NumberSequence::changeSource(INumberSource* newSource) {
    numberSource = newSource;
}

void NumberSequence::start() {
    while (true) {
        auto start = std::chrono::steady_clock::now();

        int number = numberSource->getNumber();
        if (number == -1) break;

        collection.push_back(number);
        for (auto action : actions) {
            action->execute(collection);
        }

        auto end = std::chrono::steady_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(end - start);
        if (elapsed < std::chrono::seconds(1)) {
            std::this_thread::sleep_for(std::chrono::seconds(1) - elapsed); // Keep 1 second intervals between number grabs
        } else {
            std::this_thread::sleep_for(std::chrono::seconds(1));   // Except when the source is slow, then wait another 1 second
        }

        collection.push_back(number);
    }
}