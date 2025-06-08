#include "myfactory.h"

#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

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
  for (int i = 0; i < argc / 2; ++i) {
    size_t size;
    ConstructFunc construct;
    if (myfactory(argv[1+2*i], &size, &construct) != 0) {
      printf("Failed to load plugin: %s\n", argv[1+2*i]);
      continue;
    }

    // Heap
    void* memory = malloc(size);
    construct(memory, argv[2+2*i]);
    struct Animal* animalHeap = (struct Animal*)memory;
    animalPrintGreeting(animalHeap);
    animalPrintMenu(animalHeap);

    // Stack
    memory = _malloca(size);
    construct(memory, argv[2+2*i]);
    struct Animal* animalStack = (struct Animal*)memory;
    animalPrintGreeting(animalStack);
    animalPrintMenu(animalStack);

    printf("\n");
  }

  return 0;
}