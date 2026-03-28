#include "Cell.hpp"
#include <stdexcept>
#include <limits>
#include <cmath>
#include <regex>
#include <iostream>

Cell::Cell(Sheet& sheet) : exp(""), value(std::numeric_limits<double>::quiet_NaN()), sheet(sheet) {}

bool Cell::isCircular(std::vector<Cell*> newCells) {
    for (Cell* cell : newCells) {
        if (cell == this) {
            return true;
        }
    }

    for (Cell* cell : observers) {
        return cell->isCircular(newCells);
    }

    return false;
}

void Cell::set(std::string exp) {
    std::vector<Cell*> oldRefCells; // old references to the cells that this cell depends on
    std::vector<std::string> refs = getrefs();
    for (const std::string& ref : refs) {
        oldRefCells.push_back(&sheet.cell(ref));
    }

    std::string oldexp = this->exp;
    exp = std::regex_replace(exp, std::regex("\\s+"), ""); // remove all whitespace from the expression
    this->exp = exp;    // if the expression is invalid, calculate will set the value to NaN and the NaN will be propagated to the observers

    refs = getrefs(); // get the new references to the cells that this cell depends on
    std::vector<Cell*> refCells;    // new references to the cells that this cell depends on
    for (const std::string& ref : refs) {
        refCells.push_back(&sheet.cell(ref));
    }

    // Check for circular references
    if (isCircular(refCells)) {
        this->exp = oldexp; // revert to the old expression
        throw std::runtime_error("Circular reference detected");
    }

    try {
        calculate(); // calculate the value of the cell
    } catch (std::invalid_argument& e) {
        this->exp = oldexp; // revert to the old expression
        throw e; // rethrow the exception
    }

    for (Cell* cell : oldRefCells) {
        cell->removeObserver(this); // remove this cell from the observers of the old references
    }
    for (Cell* cell : refCells) {
        cell->addObserver(this); // add this cell to the observers of the new references
    }
}

void Cell::calculate() {
    // Check if the expression is a constant
    // ^ anchor start
    // \d+ matches one or more digits
    // (\.\d+)? matches an optional decimal part
    // $ anchor end
    if (std::regex_match(exp, std::regex("^\\d+(\\.\\d+)?$"))) {
        value = std::stod(exp);
        notifyObservers();
        return;
    }

    // Check if the expression is an additive operation
    // ^ anchor start
    // ([A-Z]+[0-9]+) matches a cell reference (e.g., A1, B2, etc.)
    // \+ matches the plus sign
    // ([A-Z]+[0-9]+) matches another cell reference
    // $ anchor end
    std::regex operationRegex("^([A-Z]+[0-9]+)\\+([A-Z]+[0-9]+)$");
    std::smatch match;
    if (std::regex_match(exp, match, operationRegex)) {
        if (match.size() == 3) {
            std::string ref1 = match[1];
            std::string ref2 = match[2];

            Cell* cell1 = &sheet.cell(ref1);
            Cell* cell2 = &sheet.cell(ref2);

            if (cell1 && cell2) {
                std::pair<int, int> indices1 = sheet.cellNameToIndices(ref1);
                std::pair<int, int> indices2 = sheet.cellNameToIndices(ref2);
                if (indices1.first == -1 || indices1.second == -1 || indices2.first == -1 || indices2.second == -1) {
                    throw std::invalid_argument("Invalid cell reference: " + ref1 + " or " + ref2);
                    return;
                }

                value = cell1->getValue() + cell2->getValue();  // will return NaN if either cell is NaN
            } else {
                throw std::invalid_argument("Invalid cell reference: " + ref1 + " or " + ref2);
            }
            notifyObservers();
            return;
        }
    }

    // If the expression is invalid, throw an exception
    throw std::invalid_argument("Invalid expression: " + exp);
}

void Cell::notifyObservers() {
    for (Cell* observer : observers) {
        observer->calculate();
    }
}

double Cell::getValue() {
    return value;
}

void Cell::addObserver(Cell* cell) {
    observers.push_back(cell);
}

void Cell::removeObserver(Cell* cell) {
    observers.erase(std::remove(observers.begin(), observers.end(), cell), observers.end());
}

std::vector<std::string> Cell::getrefs() {
    std::vector<std::string> refs;
    std::regex regex("([A-Z]+[0-9]+)");
    std::smatch match;
    std::string::const_iterator searchStart(exp.cbegin());

    while (std::regex_search(searchStart, exp.cend(), match, regex)) {
        refs.push_back(match[0]);
        searchStart = match.suffix().first;
    }

    return refs;
}