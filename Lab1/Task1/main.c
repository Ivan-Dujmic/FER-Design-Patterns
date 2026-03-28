#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char const* (*PTRFUN)(); // TASK-GIVEN - UNCHANGED

char const* dogGreet(void) { // TASK-GIVEN - UNCHANGED
    return "vau!";
}
char const* dogMenu(void) { // TASK-GIVEN - UNCHANGED
    return "kuhanu govedinu";
}
char const* catGreet(void) { // TASK-GIVEN - UNCHANGED
    return "mijau!";
}
char const* catMenu(void) { // TASK-GIVEN - UNCHANGED
    return "konzerviranu tunjevinu";
}

PTRFUN dogVtable[] = {dogGreet, dogMenu};
PTRFUN catVtable[] = {catGreet, catMenu};

typedef struct Animal {
    char* name;
    PTRFUN* vtable;
} Animal; 

void animalPrintGreeting(Animal* animal) {
    printf("%s pozdravlja: %s\n", animal->name, animal->vtable[0]());
}

void animalPrintMenu(Animal* animal) {
    printf("%s voli %s\n", animal->name, animal->vtable[1]());
}

void constructAnimal(Animal* animal, char* name, PTRFUN* vtable) {
    animal->name = strdup(name);
    animal->vtable = vtable;
}

void constructDog(Animal* animal, char* name) {
    constructAnimal(animal, name, dogVtable);
}

void constructCat(Animal* animal, char* name) {
    constructAnimal(animal, name, catVtable);
}

Animal* createDog(char* name) {
    Animal* animal = (Animal*)malloc(sizeof(Animal));
    if (!animal) return NULL;
    constructDog(animal, name);
    return animal;
}

Animal* createCat(char* name) {
    Animal* animal = (Animal*)malloc(sizeof(Animal));
    if (!animal) return NULL;
    constructCat(animal, name);
    return animal;
}

void testAnimals(void){ // TASK-GIVEN - UNCHANGED
    struct Animal* p1=createDog("Hamlet");
    struct Animal* p2=createCat("Ofelija");
    struct Animal* p3=createDog("Polonije");

    animalPrintGreeting(p1);
    animalPrintGreeting(p2);
    animalPrintGreeting(p3);

    animalPrintMenu(p1);
    animalPrintMenu(p2);
    animalPrintMenu(p3);

    free(p1); free(p2); free(p3);
}

Animal* getSledDogs(int n) {
    Animal* sledDogs = (Animal*)malloc(n * sizeof(Animal));
    if (!sledDogs) return NULL;
    for (int i = 0; i < n; i++) {
        char name[20];
        sprintf(name, "SledDog%d", i + 1);
        constructDog(&sledDogs[i], name);
    }

    return sledDogs;
}

int main() {
    testAnimals();

    printf("\nHeap creation:\n");
    struct Animal* heapDog = createDog("Renato");
    Animal* heapCat = createCat("Marin");
    animalPrintGreeting(heapDog);
    animalPrintGreeting(heapCat);
    free(heapDog);
    free(heapCat);

    printf("\nStack creation:\n");
    Animal stackDog;
    constructDog(&stackDog, "Leonard");
    animalPrintGreeting(&stackDog);

    printf("\n\"Array\" creation:\n");
    int n = 6;
    Animal* sledDogs = getSledDogs(n);
    for (int i = 0; i < n; i++) {
        animalPrintGreeting(&sledDogs[i]);
    }
    free(sledDogs);

    return 0;
}