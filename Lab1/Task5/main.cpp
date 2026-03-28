using namespace std;
#include <iostream>

class B { // TASK-GIVEN - UNCHANGED
    public:
        virtual int __cdecl prva()=0;
        virtual int __cdecl druga(int)=0;
};

class D: public B { // TASK-GIVEN - UNCHANGED
    public:
        virtual int __cdecl prva(){return 42;}
        virtual int __cdecl druga(int x){return prva()+x;}
};

void callVirtualFunctionsWithoutSymbolicNames(B* pb) {
    // pb is a pointer to an object of class B - B*
    // object of class B has a pointer to vtable at the beginning - void***
    // vtable is an array of function pointers - void**
    ////////////////
    // (void*) treats pb as a pointer to void (raw address)
    // (void***) casts to a pointer to vtable
    // *(void***) dereferences to get the vtable
    void** vtable = *(void***)((void*)pb);

    typedef int(__cdecl *prva)(B*); // prva function pointer type
    typedef int(__cdecl *druga)(B*, int); // druga function pointer type
    prva f1 = (prva)vtable[0];
    druga f2 = (druga)vtable[1];
    cout << f1(pb) << '\n' << f2(pb, 1) << '\n';
}

int main() {
    callVirtualFunctionsWithoutSymbolicNames(new D());

    return 0;
}