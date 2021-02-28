
from iexfinance.refdata import get_exchange_symbols, get_iex_symbols, get_region_symbols
from iexfinance.stocks import get_historical_data, Stock
from datetime import date, timedelta
from pandas.tseries.offsets import BDay

token = 'Tsk_edf1d929fca64efa833d73000d85c60c'

def getFinancials(symbol,pe):
    result = {}
    now = date.today() - BDay(1)
    fourYearsAgo = now - BDay(1460)
    historic = get_historical_data(symbol, fourYearsAgo, fourYearsAgo, token=token)
    stockInformation = Stock(symbol,token=token)
    financials = stockInformation.get_financials(period='annual')
    quote = stockInformation.get_quote()
    information = stockInformation.get_key_stats()
    companyDesc = stockInformation.get_company()
    result['price'] = quote.loc[symbol].close
    result['company'] = information.loc[symbol].companyName
    result['peRatio'] = information.loc[symbol].peRatio
    result['volume'] = information.loc[symbol].avg30Volume
    result['yield'] = information.loc[symbol].dividendYield
    result['bookValue'] = bookValue(financials.iloc[0].shareholderEquity,pe,information.loc[symbol].sharesOutstanding)
    result['opMargin'] = operatingMargin(financials.iloc[0].operatingIncome,financials.iloc[0].revenue)
    result['yrPrice'] = historic.loc[fourYearsAgo.strftime('%Y-%m-%d')].close
    result['description'] = companyDesc.loc[symbol].description
    result['symbol'] = symbol
    return result

def bookValue(se,pe,cs):
    if type(pe) == type(1) and pe != 0:
        value = (se-pe)/cs
        return value
    else:
        value = se/cs
        return value

def operatingMargin(opr,rev):
    result = opr / rev
    return result

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