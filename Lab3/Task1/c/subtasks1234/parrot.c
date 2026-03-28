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

void* create(char const* name) {
    struct Parrot* t = malloc(sizeof(struct Parrot));
    if (!t) return NULL;
    t->vptr = vtable;
    t->name = strdup(name);
    return t;
}