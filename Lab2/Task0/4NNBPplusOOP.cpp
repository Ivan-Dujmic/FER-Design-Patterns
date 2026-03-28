#include <iostream>
#include <assert.h>
#include <stdlib.h>
#include <list>

struct Point {
    int x; int y;
};

class Shape {
    public:
        virtual void draw()=0;
        virtual void move(int, int)=0;
};

class Circle : public Shape {
    private:
        double radius_;
        Point center_;

    public:
        virtual void draw() {
            std::cerr << "in drawCircle: x: " << center_.x << ", y: " << center_.y << ", r: " << radius_ << "\n";
        }

        virtual void move(int trans_x, int trans_y) {
            std::cerr << "in moveCircle\n";
            center_.x += trans_x;
            center_.y += trans_y;
        }
};

class Square : public Shape {
    private:
        double side_;
        Point center_;

    public:
        virtual void draw() {
            std::cerr << "in drawSquare: x: " << center_.x << ", y: " << center_.y << ", side: " << side_ << "\n";
        }

        virtual void move(int trans_x, int trans_y) {
            std::cerr << "in moveCircle\n";
            center_.x += trans_x;
            center_.y += trans_y;
        }
};

class Rhomb : public Shape {
    private:
        double side_;
        Point center_;

    public:
        virtual void draw() {
            std::cerr << "in drawRhomb: x: " << center_.x << ", y: " << center_.y << ", side: " << side_ << "\n";
        }

        virtual void move(int trans_x, int trans_y) {
            std::cerr << "in moveCircle\n";
            center_.x += trans_x;
            center_.y += trans_y;
        }
};

void drawShapes(const std::list<Shape*>& fig) {
    std::list<Shape*>::const_iterator it;
    for (it = fig.begin() ; it != fig.end() ; ++it) {
        (*it)->draw();
    }
}

void moveShapes(const std::list<Shape*>& fig, int trans_x, int trans_y) {
    std::list<Shape*>::const_iterator it;
    for (it = fig.begin() ; it != fig.end() ; ++it) {
        (*it)->move(trans_x, trans_y);
    }
}

int main() {
    std::list<Shape*> shapes;
    shapes.push_back(new Circle());
    shapes.push_back(new Square());
    shapes.push_back(new Square());    
    shapes.push_back(new Rhomb());

    drawShapes(shapes);
    moveShapes(shapes, 1, 2);
    drawShapes(shapes);
}