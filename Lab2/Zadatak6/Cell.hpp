#pragma once
#include "Sheet.hpp"
#include <string>
#include <vector>

class Sheet;

class Cell {
    private:
        friend class Sheet;

        std::string exp;    // expression
        double value;   // current value of the cell
        std::vector<Cell*> observers;   // list of Cells that depend on this cell
        Sheet& sheet; // reference to the sheet

        Cell(Sheet& sheet);

        ~Cell() = default;

        bool isCircular(std::vector<Cell*> newCells);    // checks if the new cells are already down the chain of observers, returns true if circular reference is detected

        void set(std::string exp);   // sets the expression of the cell and propagates the change

        void calculate();   // calculates the value of the cell

        double getValue();    // returns the value of the cell

        void addObserver(Cell* cell);    // adds a cell to the list of observers

        void removeObserver(Cell* cell); // removes a cell from the list of observers

        void notifyObservers();   // notifies all observers of the change (makes them recalculate)

        std::vector<std::string> getrefs();  // returns a vector of all cells that the cell depends on
};