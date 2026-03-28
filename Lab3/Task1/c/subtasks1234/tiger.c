#include <stdlib.h>
#include <string.h>

typedef char const* (*PTRFUN)(void*);

struct Tiger {
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
    struct Tiger* t = (struct Tiger*)this;
    return t->name;
}

static char const* greet(void* this) {
    return "Mijau!";
}

static char const* menu(void* this) {
    return "mlako mlijeko";
}

void* create(char const* name) {
    struct Tiger* t = malloc(sizeof(struct Tiger));
    if (!t) return NULL;
    t->vptr = vtable;
    t->name = strdup(name);
    return t;
}