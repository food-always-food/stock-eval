
from iexfinance.refdata import get_exchange_symbols, get_iex_symbols, get_region_symbols
from iexfinance.stocks import get_historical_data, Stock
from datetime import date, timedelta
from pandas.tseries.offsets import BDay


def getFinancials(symbol):
    now = date.today() - BDay(1)
    print(now.strftime('%Y-%m-%d'))
    mostRecent = get_historical_data(symbol, now, now,token='Tsk_edf1d929fca64efa833d73000d85c60c')
    print(mostRecent.loc[now.strftime('%Y-%m-%d')].close)
    print(mostRecent.loc[now.strftime('%Y-%m-%d')].volume)
    fourYearsAgo = now - BDay(1460)
    print(fourYearsAgo)
    historic = get_historical_data(symbol, fourYearsAgo, fourYearsAgo, token='Tsk_edf1d929fca64efa833d73000d85c60c')
    print(historic)
    stockInformation = Stock(symbol,token='Tsk_edf1d929fca64efa833d73000d85c60c')
    company = stockInformation.get_company()
    financials = stockInformation.get_financials()
    quote = stockInformation.get_quote()
    print(financials.iloc[0])
    print(company.loc[symbol])
    print(quote.loc[symbol])
    return None

test = getFinancials("AAPL")


# mostRecent = get_historical_data("AAPL", now, now,  output_format='json',token='Tsk_edf1d929fca64efa833d73000d85c60c')
# fourYearsAgo = get_historical_data("AAPL",yearAgo,yearAgo, token='Tsk_edf1d929fca64efa833d73000d85c60c')
# stockInformation = Stock("AAPL",token='Tsk_edf1d929fca64efa833d73000d85c60c')
# price = stockInformation.get_price()
# print(mostRecent)
# print(fourYearsAgo)
# print(price)
# print(historical)

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