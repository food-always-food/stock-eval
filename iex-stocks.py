import pandas as pd
from iexfinance.refdata import get_exchange_symbols, get_iex_symbols, get_region_symbols
from iexfinance.stocks import get_historical_data, Stock

import pandas as pd
from iexfinance.refdata import get_exchange_symbols, get_iex_symbols, get_region_symbols
from iexfinance.stocks import get_historical_data, Stock

# Note that current ENV varriable has this working on IEX Sandbox 

# Begin by getting all available symbols from the system and convert to a list
test = get_region_symbols('ca',token='Tsk_edf1d929fca64efa833d73000d85c60c')
# test = get_exchange_symbols('tsx',token='Tsk_edf1d929fca64efa833d73000d85c60c')
# test = get_iex_symbols(token='Tsk_edf1d929fca64efa833d73000d85c60c')
print(test)
symbols = test['symbol'].values.tolist()
# print(symbols)

TenDollarStock = []

for x in symbols:
    test = Stock(x,token='Tsk_edf1d929fca64efa833d73000d85c60c')
    price = test.get_price()
    try:
        if price.loc['price',x] <= 10 and price.loc['price',x] >= 5:
            stock = {"Symbol":x,"Price":price.loc['price',x]}
            TenDollarStock.append(stock)
            print(TenDollarStock)
    except KeyboardInterrupt:
        exit()
    except:
        pass
    print(price)
# result = get_historical_data("AAPL", start="20200101",output_format='pandas',token='Tsk_edf1d929fca64efa833d73000d85c60c')
# print(result.head())

# result['high-low-difference'] = ((result['high']-result['low'])/result['low'])
# print(result)

export = pd.DataFrame.from_dict(TenDollarStock)
export.to_csv("Ten Dolar Stock CA.csv")