#include "myfactory.h"
#include "animal.h"

#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

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