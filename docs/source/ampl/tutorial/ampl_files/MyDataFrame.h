#pragma once

#include <iostream>     // For std::cout
#include <string>       // For std::string
#include <vector>       // For vector
#include <algorithm>    // For max_element
#include <limits>       // For numeric_limits
#include <iomanip>      // For setw()
#include <sstream>      // For stringstream

constexpr double myNaN = std::numeric_limits<double>::quiet_NaN();

// Struct for storing strings or doubles
// Will be used as an element of a custom C++ DataFrame 
// called MyDataFrame (a vector of MyDataPoint vectors)
struct MyDataPoint {
    enum class Type { Double, String, Empty };

    Type type;
    double doubleValue;
    std::string stringValue;

    MyDataPoint() : type(Type::Empty), 
                    stringValue(""), 
                    doubleValue(myNaN) {}

    MyDataPoint(double value) : type(Type::Double), 
                                stringValue(""), 
                                doubleValue(value) {}

    MyDataPoint(const char* value) : type(Type::String), 
                                     stringValue(value), 
                                     doubleValue(myNaN) {}

    MyDataPoint(const std::string& value) : type(Type::String), 
                                            stringValue(value), 
                                            doubleValue(myNaN) {}

    ~MyDataPoint() 
    {
        stringValue.~basic_string();
    }
};

// Create type aliases
using MyDataCol = std::vector<MyDataPoint>;
using MyDataFrame = std::vector<MyDataCol>;

// A custom printer function for MyDataFrame objects
void printMyDataFrame(const MyDataFrame& df) 
{
    if (&df == nullptr) {
        std::cerr << "No datafarme to print!" << std::endl;
        return;
    }
    std::size_t numRows = df[0].size();
    std::size_t numCols = df.size();
    
    // Find the maximum width for each column 
    // so we can align columns when printing
    std::vector<std::size_t> columnWidths(numRows);
    for (std::size_t col = 0; col < numCols; ++col) {
        for (std::size_t row = 0; row < numRows; ++row) {
            const MyDataPoint& point = df[col][row];
            if(point.type == MyDataPoint::Type::String) {
                columnWidths[row] = std::max(columnWidths[row], point.stringValue.size());
            }
            else {
                std::stringstream ss;            
                ss << std::fixed << std::setprecision(2) << point.doubleValue;
                columnWidths[row] = std::max(columnWidths[row], ss.str().size());
            }
        }
    }
    // Find the maximum width of the maximum column widths
    auto maxIndex = std::max_element(columnWidths.begin(), columnWidths.end());
    auto maxWidth = *maxIndex;

    // Print MyDataFrame row by row and align output
    for (std::size_t row = 0; row < numRows; ++row) {
        for (std::size_t col = 0; col < numCols; ++col) {
            const MyDataPoint& point = df[col][row];
            if (point.type == MyDataPoint::Type::Double) {
                std::cout << std::setw(maxWidth + 1) << std::right << point.doubleValue;
            } 
            else if (point.type == MyDataPoint::Type::String) {
                std::cout << std::setw(maxWidth + 1) << std::left << point.stringValue; 
            } 
            else if (point.type == MyDataPoint::Type::Empty) {
                std::cout << std::setw(maxWidth + 1) << std::right << "...";
            }
        }
        std::cout << std::endl;
    }
}
