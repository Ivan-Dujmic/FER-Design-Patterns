#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*
I couldn't find a way to achieve these 3 at the same time, only 2 at a time:
1. Private variables
2. Heap and stack allocation
3. Using an actual object (Unary_Function) and not a pointer to that object (*Unary_Function)

Private variables can be achieved by having an additional .c file, 
but then we can't know the size of that object with sizeof
which is necessary for malloc and stack allocation.
It would be possible to make a function that returns the size of the object or constructors for different allocations,
but to achieve the stack allocation we would have to use a pointer to the object anyway
which is messy and can introduce other problems.

So I decided to leave out the private variables
*/

typedef struct Unary_Function Unary_Function;

typedef struct {
    double (*value_at)(Unary_Function*, double);
    double (*negative_value_at)(Unary_Function*, double);
} Unary_Function_Vtable;

typedef struct Unary_Function {
    Unary_Function_Vtable* vtable;
    int lower_bound;
    int upper_bound;
} Unary_Function;

double default_negative_value_at(Unary_Function* f, double x) {
    return -f->vtable->value_at(f, x);
}

void tabulate(Unary_Function* this) {
    for(int x = this->lower_bound ; x <= this->upper_bound ; x++) {
        printf("f(%d)=%lf\n", x, this->vtable->value_at(this, x));
    }
};

bool same_functions_for_ints(Unary_Function *uf1, Unary_Function *uf2, double tolerance) {
    if(uf1->lower_bound != uf2->lower_bound || uf1->upper_bound != uf2->upper_bound) return false;
    for(int x = uf1->lower_bound; x <= uf1->upper_bound; x++) {
        double delta = uf1->vtable->value_at(uf1, x) - uf2->vtable->value_at(uf2, x);
        if(delta < 0) delta = -delta;
        if(delta > tolerance) return false;
    }
    return true;
};

typedef struct Square {
    Unary_Function base;
} Square;

double square_value_at(Unary_Function* f, double x) {
    return x * x;
}

Unary_Function_Vtable Square_Vtable = {
    .value_at = square_value_at,
    .negative_value_at = default_negative_value_at
};

void constructSquare(Square* square, int lb, int ub) {
    square->base.vtable = &Square_Vtable;
    square->base.lower_bound = lb;
    square->base.upper_bound = ub;
}

Square* createSquare(int lb, int ub) {
    Square* square = (Square*)malloc(sizeof(Square));
    if (!square) return NULL;
    constructSquare(square, lb, ub);
    return square;
}

typedef struct Linear {
    Unary_Function base;
    double a;
    double b;
} Linear;

double linear_value_at(Unary_Function* f, double x) {
    Linear* linear = (Linear*)f;
    return linear->a * x + linear->b;
}

Unary_Function_Vtable Linear_Vtable = {
    .value_at = linear_value_at,
    .negative_value_at = default_negative_value_at
};

void constructLinear(Linear* linear, int lb, int ub, double a_coef, double b_coef) {
    linear->base.vtable = &Linear_Vtable;
    linear->base.lower_bound = lb;
    linear->base.upper_bound = ub;
    linear->a = a_coef;
    linear->b = b_coef;
}

Linear* createLinear(int lb, int ub, double a_coef, double b_coef) {
    Linear* linear = (Linear*)malloc(sizeof(Linear));
    if (!linear) return NULL;
    constructLinear(linear, lb, ub, a_coef, b_coef);
    return linear;
}

int main() {
    Square *f1 = createSquare(-2, 2);
    tabulate((Unary_Function*) f1);
    Linear *f2 = createLinear(-2, 2, 5, -2);
    tabulate((Unary_Function*) f2);
    printf("f1==f2: %s\n", same_functions_for_ints((Unary_Function*) f1, (Unary_Function*) f2, 1E-6) ? "DA" : "NE");
    printf("neg_val f2(1) = %lf\n", f2->base.vtable->negative_value_at((Unary_Function*) f2, 1.0));
    free(f1);
    free(f2);

    return 0;
}
