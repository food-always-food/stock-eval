
from iexfinance.refdata import get_exchange_symbols, get_iex_symbols, get_region_symbols
from iexfinance.stocks import get_historical_data, Stock
from datetime import datetime, timedelta
from pandas.tseries.offsets import BDay

now = datetime.now() - BDay(1)
print(now)
yearAgo = now - BDay(365)
print(yearAgo)


historical = get_historical_data("APPL",)
stockInformation = Stock("APPL",token='Tsk_edf1d929fca64efa833d73000d85c60c')
print(stockInformation)

# for x in symbols:
#     test = Stock(x,token='Tsk_edf1d929fca64efa833d73000d85c60c')
#     price = test.get_price()
#     try:
#         if price.loc['price',x] <= 10 and price.loc['price',x] >= 5:
#             stock = {"Symbol":x,"Price":price.loc['price',x]}
#             TenDollarStock.append(stock)
#             print(TenDollarStock)
#     except KeyboardInterrupt:
#         exit()
#     except:
#         pass
#     print(price)
# # result = get_historical_data("AAPL", start="20200101",output_format='pandas',token='Tsk_edf1d929fca64efa833d73000d85c60c')
# # print(result.head())

# # result['high-low-difference'] = ((result['high']-result['low'])/result['low'])
# # print(result)

# export = pd.DataFrame.from_dict(TenDollarStock)
# export.to_csv("Ten Dolar Stock CA.csv")