from iexfinance.refdata import get_exchange_symbols, get_iex_symbols, get_region_symbols
from iexfinance.stocks import get_historical_data, Stock
from datetime import date, timedelta
from pandas.tseries.offsets import BDay
import os

token = os.environ["TOKEN"]


def getFinancials(symbol, pe):
    result = {}
    try:
        now = date.today() - BDay(1)
        fourYearsAgo = now - BDay(1460)
        historic = get_historical_data(symbol, fourYearsAgo, fourYearsAgo, token=token)
        stockInformation = Stock(symbol, token=token)
        financials = stockInformation.get_financials(period="annual")
        quote = stockInformation.get_quote()
        print(quote)
        information = stockInformation.get_key_stats()
        companyDesc = stockInformation.get_company()
        result["price"] = quote.loc[symbol].latestPrice
        result["company"] = information.loc[symbol].companyName
        result["peRatio"] = information.loc[symbol].peRatio
        result["volume"] = information.loc[symbol].avg30Volume
        result["yield"] = information.loc[symbol].dividendYield
        result["bookValue"] = bookValue(
            financials.iloc[0].shareholderEquity,
            pe,
            information.loc[symbol].sharesOutstanding,
        )
        result["opMargin"] = operatingMargin(
            financials.iloc[0].operatingIncome, financials.iloc[0].revenue
        )
        result["yrPrice"] = historic.loc[fourYearsAgo.strftime("%Y-%m-%d")].close
        result["description"] = companyDesc.loc[symbol].description
        result["symbol"] = symbol
        result["status"] = "success"
        return result
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        return result


def bookValue(se, pe, cs):
    if type(pe) == type(1) and pe != 0:
        value = (se - pe) / cs
        return value
    else:
        value = se / cs
        return value


def operatingMargin(opr, rev):
    result = opr / rev
    return result
