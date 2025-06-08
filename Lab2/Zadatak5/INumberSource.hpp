#pragma once

class INumberSource {
    public:
        virtual ~INumberSource() = default;

        virtual int getNumber() = 0;
};