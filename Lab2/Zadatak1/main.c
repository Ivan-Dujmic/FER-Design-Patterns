#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const void* mymax(  // PARAMETERS ARE TASK-GIVEN
    // base - pointer to the first element of the array
    // nmemb - number of elements in the array
    // size - size of each element in the array
    // compar - function pointer to the comparison function (if first > second => return 1 ; else => return 0)
    const void *base, size_t nmemb, size_t size,
    int (*compar)(const void *, const void *)
) {
    if (nmemb == 0) return NULL;

    const void* max = base;
    for (size_t i = 1; i < nmemb; i++) {
        const void* current = (const char*)base + i * size; // we have to use char* instead of void* to do pointer arithmetic
        if (compar(current, max) == 1) max = current;
    }
    return max;
}

int gt_int(const void* a, const void* b) {
    return *(int*)a > *(int*)b ? 1 : 0;
}

int gt_char(const void* a, const void* b) {
    return *(char*)a > *(char*)b ? 1 : 0;
}

int gt_str(const void* a, const void* b) {
    // strcmp will return positive if a > b
    return strcmp(*(const char**)a, *(const char**)b) > 0 ? 1 : 0;
}

int main() {
    int arr_int[] = { 1, 3, 5, 7, 4, 6, 9, 2, 0 };  // TASK-GIVEN
    char arr_char[] = "Suncana strana ulice"; // TASK-GIVEN
    const char* arr_str[] = {   // TASK_GIVEN
       "Gle", "malu", "vocku", "poslije", "kise",
       "Puna", "je", "kapi", "pa", "ih", "njise"
    };

    int max_int = *(int*) mymax(arr_int, sizeof(arr_int) / sizeof(arr_int[0]), sizeof(int), gt_int);
    char max_char = *(char*) mymax(arr_char, sizeof(arr_char) / sizeof(arr_char[0]), sizeof(char), gt_char);
    const char* max_str = *(const char**) mymax(arr_str, sizeof(arr_str) / sizeof(arr_str[0]), sizeof(char*), gt_str);

    printf("Max int: %d\n", max_int);
    printf("Max char: %c\n", max_char);
    printf("Max string: %s\n", max_str);

    return 0;
}