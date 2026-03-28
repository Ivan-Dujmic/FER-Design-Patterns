#include "Cell.hpp"
#include "Sheet.hpp"
#include <iostream>

int main() {
    Sheet sheet(5, 5);

    // Constant
    sheet.set(sheet.cell("A1"), "5");
    std::cout << "A1: " << sheet.evaluate(sheet.cell("A1")) << std::endl;   // should print 5

    // Additive operation between two constants
    sheet.set(sheet.cell("A2"), "10");
    sheet.set(sheet.cell("A3"), "A1+A2");
    std::cout << "A3: " << sheet.evaluate(sheet.cell("A3")) << std::endl;   // should print 15

    // A0 is out of bounds
    try {
        sheet.set(sheet.cell("A0"), "A1+A2");    // should throw an error (out of bounds)
    } catch (std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    // Additive operation between constant and cell reference
    sheet.set(sheet.cell("A4"), "A1+A3");
    std::cout << "A4: " << sheet.evaluate(sheet.cell("A4")) << std::endl;   // should print 20

    // Z2 is out of bounds
    try {
        sheet.set(sheet.cell("B1"), "A1+Z2");
    } catch (std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;   // should throw an error (out of bounds)
    }

    // B1 should be empty (not set yet) and return nan
    std::cout << "B1: " << sheet.evaluate(sheet.cell("B1")) << std::endl;   // should print nan

    // Invalid expression A-B1
    try {
        sheet.set(sheet.cell("B2"), "A-B1");
    } catch (std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;   // should throw an error (invalid expression)
    }

    // B2 should be empty (not set yet) and return nan
    std::cout << "B2: " << sheet.evaluate(sheet.cell("B2")) << std::endl;   // should print nan

    // B4 references B3 and then B3 references B4 (circular reference)
    sheet.set(sheet.cell("B3"), "12");
    sheet.set(sheet.cell("B4"), "A4+B3");
    try {
        sheet.set(sheet.cell("B3"), "A4+B4");    // should throw an error (circular reference)
    } catch (std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    
    // B3 should still be 12
    std::cout << "B3: " << sheet.evaluate(sheet.cell("B3")) << std::endl;   // should print 12

    // nan + cell = nan
    sheet.set(sheet.cell("B5"), "B2+A1");
    std::cout << "B5: " << sheet.evaluate(sheet.cell("B5")) << std::endl;   // should print nan

    // Updating B2 should change B5
    sheet.set(sheet.cell("B2"), "100");
    std::cout << "A1: " << sheet.evaluate(sheet.cell("A1")) << std::endl;   // should print 5
    std::cout << "B2: " << sheet.evaluate(sheet.cell("B2")) << std::endl;   // should print 100
    std::cout << "B5: " << sheet.evaluate(sheet.cell("B5")) << std::endl;   // should print 105

    // Updating B2 should change C1 (and B5)
    sheet.set(sheet.cell("C1"), "B5+B2");
    std::cout << "C1: " << sheet.evaluate(sheet.cell("C1")) << std::endl;   // should print 205
    sheet.set(sheet.cell("B2"), "200");
    std::cout << "C1: " << sheet.evaluate(sheet.cell("C1")) << std::endl;   // should print 405

    // Big indexing
    Sheet bigSheet(1000, 1000);
    std::cout << "ALL1000: " << bigSheet.evaluate(bigSheet.cell("ALL1000")) << std::endl; // should print nan
    try {
        std::cout << "ALL1001: " << bigSheet.evaluate(bigSheet.cell("ALL1001")) << std::endl; // should throw an error (out of bounds)
    } catch (std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    try {
        std::cout << "ALM1000: " << bigSheet.evaluate(bigSheet.cell("ALM1000")) << std::endl; // should throw an error (out of bounds)
    } catch (std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    return 0;
}