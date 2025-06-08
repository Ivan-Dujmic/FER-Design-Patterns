#include <stdlib.h>
#include <string.h>

typedef char const* (*PTRFUN)(void*);

struct Parrot {
    PTRFUN* vptr;
    char* name;
};

// Static because they should be private to this file
static char const* name(void* this);
static char const* greet(void* this);
static char const* menu(void* this);

static PTRFUN vtable[] = {
    name,
    greet,
    menu
};

static char const* name(void* this) {
    struct Parrot* t = (struct Parrot*)this;
    return t->name;
}

static char const* greet(void* this) {
    return "Sto mu gromova!";
}

static char const* menu(void* this) {
    return "brazilske orahe";
}

size_t sizeof_object(void) {
    return sizeof(struct Parrot);
}

void construct(void* memory, const char* name) {
    struct Parrot* p = (struct Parrot*)memory;
    p->vptr = vtable;
    p->name = strdup(name);
}