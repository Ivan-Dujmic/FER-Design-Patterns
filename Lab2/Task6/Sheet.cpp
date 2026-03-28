#include "Sheet.hpp"
#include <stdexcept>

Sheet::Sheet(int cols, int rows) : cols(cols), rows(rows) {
    if (cols <= 0 || rows <= 0) {
        throw std::invalid_argument("Invalid number of rows or columns");
    }
    cells.resize(cols);
    for (int i = 0; i < cols; i++) {
        cells[i].resize(rows);
        for (int j = 0; j < rows; j++) {
            cells[i][j] = new Cell(*this); // create a new cell in the sheet
        }
    }
}

Sheet::~Sheet() { /* Handled automatically */ }

Cell& Sheet::cell(std::string cellName) {
    std::pair<int, int> indices = cellNameToIndices(cellName);

    if (indices.first == -1 || indices.second == -1) {
        throw std::invalid_argument("Invalid cell name");
    }

    return *cells[indices.first][indices.second];
}

void Sheet::set(Cell& ref, std::string exp) {
    ref.set(exp);
}

std::vector<Cell*> Sheet::getrefs(Cell& cell) {
    std::vector<Cell*> refs;
    std::vector<std::string> strrefs = cell.getrefs();
    for (const auto& strref : strrefs) {
        std::pair<int, int> indices = cellNameToIndices(strref);
        if (indices.first != -1 && indices.second != -1) {
            refs.push_back(cells[indices.first][indices.second]);
        }
    }

    return refs;
}

double Sheet::evaluate(Cell& cell) {
    return cell.getValue();
}

std::pair<int, int> Sheet::cellNameToIndices(std::string cellName) {
    int col = 0;
    int row = 0;

    bool readingLetters = true;

    for (size_t i = 0; i < cellName.size(); i++) {
        if (cellName[i] >= 'A' && cellName[i] <= 'Z') {
            if (readingLetters) {
                col = col * 26 + (cellName[i] - 'A' + 1);
            } else {
                return std::make_pair(-1, -1); // was expecting a number
            }
        } else if (cellName[i] >= '0' && cellName[i] <= '9' && i > 0) {
            readingLetters = false;
            row = row * 10 + (cellName[i] - '0');
        } else {
            return std::make_pair(-1, -1); // invalid character or start with number
        }
    }

    if (row == 0 || row > rows || col > cols) {
        return std::make_pair(-1, -1); // rows start from 1
    }

    return std::make_pair(col - 1, row - 1); // convert to 0-based index
}