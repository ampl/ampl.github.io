from amplpy import DataFrame
import pandas as pd

def set_data(ampl, data_name):

    if data_name == "lemonade":
        PROD = ['lemonade', 'iced_tea']
        INGR = ['lemon', 'tea_bag', 'sugar']
        profit_per_product_data = [1.5, 1.0]
        limit_data = [10, 8, 20]
        usage_data = [1.0, 0.0,
                      0.0, 1.0,
                      2.0, 1.0]
    elif data_name == "mulled_wine":
        PROD = ["mulled_wine", "hot_tea"]
        INGR = ["spice", "tea_bag", "sugar", "wine"]
        profit_per_product_data = [2.0, 1.5]
        limit_data = [12, 8, 30, 15]
        usage_data = [2.0, 0.0,
                      0.0, 1.0,
                      4.0, 2.0,
                      2.0, 0.0]
    else:
        raise ValueError("Invalid data_name. Data cannot be set.")
    
    ampl.param["fee"] = 2.0
    ampl.set["PROD"] = PROD
    ampl.set["INGR"] = INGR
    profit_per_product = pd.DataFrame(  profit_per_product_data, 
                                        index=PROD, 
                                        columns=["profit_per_product"] )
    ampl.set_data(profit_per_product)
    limit = pd.DataFrame( { 'limit': limit_data },
                            index=INGR )
    ampl.set_data(limit) 
    usage = pd.DataFrame( { 'usage': usage_data }, 
                            index=pd.MultiIndex.from_tuples([(i,j) for i in INGR for j in PROD]) )
    ampl.set_data(usage)
