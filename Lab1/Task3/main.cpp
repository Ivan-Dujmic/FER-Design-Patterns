#include <stdio.h>

#pragma pack(push, 4)
class PackedCoolClass {
    public:
        virtual void set(int x){x_=x;};
        virtual int get(){return x_;};
    private:
        int x_;
};
#pragma pack(pop)

class CoolClass {
    public:
        virtual void set(int x){x_=x;};
        virtual int get(){return x_;};
    private:
        int x_;
};

class PlainOldClass {
    public:
        void set(int x){x_=x;};
        int get(){return x_;};
    private:
        int x_;
};

int main() {
    printf("sizeof(PlainOldClass) = %d\nsizeof(CoolClass) = %d\nsizeof(PackedCoolClass) = %d\n\n", sizeof(PlainOldClass), sizeof(CoolClass), sizeof(PackedCoolClass));
    printf("alignof(PlainOldClass) = %d\nalignof(CoolClass) = %d\nalignof(PackedCoolClass) = %d\n", alignof(PlainOldClass), alignof(CoolClass), alignof(PackedCoolClass));

    return 0;
}