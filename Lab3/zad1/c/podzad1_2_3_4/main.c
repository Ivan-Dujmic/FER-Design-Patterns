#include "myfactory.h"

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

int main(int argc, char *argv[]) {
  for (int i=0 ; i<argc/2 ; ++i) {
    struct Animal* p = (struct Animal*)myfactory(argv[1+2*i], argv[1+2*i+1]);
    if (!p) {
      printf("Creation of plug-in object %s failed.\n", argv[1+2*i]);
      continue;
    }

    animalPrintGreeting(p);
    animalPrintMenu(p);
    free(p); 
  }
}