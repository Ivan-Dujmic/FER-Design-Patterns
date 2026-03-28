#pragma once

#ifdef __cplusplus
extern "C" {
#endif

struct Animal;

void animalPrintGreeting(struct Animal* animal);
void animalPrintMenu(struct Animal* animal);

#ifdef __cplusplus
}
#endif