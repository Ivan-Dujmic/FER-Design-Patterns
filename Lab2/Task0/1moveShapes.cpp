#include <iostream>
#include <assert.h>
#include <stdlib.h>

struct Point {
    int x; int y;
};

struct Shape {
    enum EType {circle, square};
    EType type_;
};

struct Circle {
    Shape::EType type_;
    double radius_;
    Point center_;
};

struct Square {
    Shape::EType type_;
    double side_;
    Point center_;
};

void drawSquare(struct Square*) {
    std::cerr <<"in drawSquare\n";
}

void drawCircle(struct Circle*) {
    std::cerr <<"in drawCircle\n";
}

void drawShapes(Shape** shapes, int n) {
    for (int i=0; i<n; ++i) {
        struct Shape* s = shapes[i];
        switch (s->type_) {
            case Shape::square:
                drawSquare((struct Square*)s);
                break;
            case Shape::circle:
                drawCircle((struct Circle*)s);
                break;
            default:
                assert(0); 
                exit(0);
        }
    }
}

void printCenters(Shape** shapes, int n) {
    for (int i=0; i<n; ++i) {
        struct Shape* s = shapes[i];
        switch (s->type_) {
            case Shape::square:
                std::cerr << "Square center: (" << ((struct Square*)s)->center_.x << ", " << ((struct Square*)s)->center_.y << ")\n";
                break;
            case Shape::circle:
                std::cerr << "Circle center: (" << ((struct Circle*)s)->center_.x << ", " << ((struct Circle*)s)->center_.y << ")\n";
                break;
            default:
                assert(0); 
                exit(0);
        }
    }
}

void moveShapes(Shape** shapes, int n, int trans_x, int trans_y) {
    std::cerr << "in moveShapes\n";
    for (int i = 0 ; i < n ; i++) {
        struct Shape* s = shapes[i];
        switch (s->type_) {
            case Shape::square:
                ((struct Square*)s)->center_.x += trans_x;
                ((struct Square*)s)->center_.y += trans_y;
                break;
            case Shape::circle:
                ((struct Circle*)s)->center_.x += trans_x;
                ((struct Circle*)s)->center_.y += trans_y;
                break;
            default:
                assert(0); 
                exit(0);
        }
    }
}

int main(){
    Shape* shapes[4];
    shapes[0]=(Shape*)new Circle;
    shapes[0]->type_=Shape::circle;
    shapes[1]=(Shape*)new Square;
    shapes[1]->type_=Shape::square;
    shapes[2]=(Shape*)new Square;
    shapes[2]->type_=Shape::square;
    shapes[3]=(Shape*)new Circle;
    shapes[3]->type_=Shape::circle;

    drawShapes(shapes, 4);

    printCenters(shapes, 4);
    moveShapes(shapes, 4, 1, 2);
    printCenters(shapes, 4);
}