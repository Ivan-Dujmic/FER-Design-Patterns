#include <stdio.h>
#include <stdlib.h>

typedef char const* (*PTRFUN)(void*);

struct Animal {
  PTRFUN* vptr;
  // vtable entries:
  // 0: char const* name(void* this);
  // 1: char const* greet();
  // 2: char const* menu();
};

void animalPrintGreeting(struct Animal* animal) {
  printf("%s pozdravlja: %s\n", animal->vptr[0](animal), animal->vptr[1](animal));
}

void animalPrintMenu(struct Animal* animal) {
  printf("%s voli %s\n", animal->vptr[0](animal), animal->vptr[2](animal));
}