#pragma once

#include "MyDataFrame.h"
#include "ampl/ampl.h"

// Load data from an ampl::DataFrame that only contains a collection of
// non-indexed AMPL entities into MyDataFrame
std::unique_ptr<MyDataFrame> transpose1D(ampl::DataFrame &adf)
{
    std::size_t index = adf.getNumIndices();

    // Check to make sure that AMPL entities are not indexed
    if (index == 0) {
   
        // Create a pointer to MyDataFrame to be returned
        auto mdf_ptr = std::make_unique<MyDataFrame>();
        auto& mdf = *mdf_ptr;  /// So we can use dot i.e. '.' to access methods.
   
        // Get entity names by reading the header of ampl::DataFrame
        auto items = adf.getHeaders();
        // Get the values for each entity by reading the first row of ampl::DataFrame
        auto values = adf.getRowByIndex(index);
   
        // Will be used to store entity names 
        MyDataCol myItemsCol;
        // Will be used to store entity values
        MyDataCol myValuesCol;
       
        // Create a heading for the first column containing entity names
        myItemsCol.push_back(MyDataPoint("item"));
        // Add entity names to the first column
        for (const auto& item : items) {
            myItemsCol.push_back(MyDataPoint(item));
        }
        // Add the first column to the MyDataFrame to be returned
        mdf.push_back(myItemsCol);
        
        // Create a heading for the second column containing entity values
        myValuesCol.push_back(MyDataPoint("value"));
        // Add entity values to the second column
        for (const auto& value : values) {
            myValuesCol.push_back(MyDataPoint(value.dbl()));
        }
        // Add the second column to the MyDataFrame to be returned
        mdf.push_back(myValuesCol); 
        
        return mdf_ptr;
    }
    else {
        std::cerr << "Cannot transform indexed AMPL entities!" << std::endl;
        return nullptr;
    }
}
