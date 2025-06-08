#pragma once
#include "INumberSource.hpp"

class KeyboardSource : public INumberSource {
    public:
        KeyboardSource() = default;

        ~KeyboardSource() = default;

        int getNumber() override;
};