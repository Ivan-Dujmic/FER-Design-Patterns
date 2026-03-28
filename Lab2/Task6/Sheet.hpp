#pragma once
#include "Cell.hpp"
#include <string>
#include <vector>
#include <utility>

class Cell;

class Sheet {
    private:
        int cols;   // number of columns (marked with letters A, B, C, ..., Z, AA, AB, ...)
        int rows;   // number of rows (marked with numbers)
        std::vector<std::vector<Cell*>> cells; // 2D array of cells (cells[0][0] is A1, cells[1][0] is B1, etc.)

    public:
        Sheet(int rows, int cols);

        ~Sheet();

        Cell& cell(std::string cellName);   // returns a reference to the cell with the given name

        void set(Cell& ref, std::string exp);   // sets the expression of the cell and propagates the change

        std::vector<Cell*> getrefs(Cell& cell); // returns a vector of all cells that the given cell depends on

        double evaluate(Cell& cell);    // returns the value of the cell (the evaluation is done by the set method)
       
        std::pair<int, int> cellNameToIndices(std::string cellName);    // will return (-1, -1) if the cell name is invalid or out of bounds
};