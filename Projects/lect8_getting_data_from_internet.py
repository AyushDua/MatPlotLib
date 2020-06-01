import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import urllib.request

# def bytespdate2num(fmt,encoding='utf-8'):
#     strconverter = mdates.strpdate2num(fmt)
#     def bytesconverter(b):
#         s = b.decode(encoding)
#         return strconverter(s)
#     return bytesconverter


def graph_stock():
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line=line.split(',')
        if len(split_line)==7:
            if 'Volume' not in line and 'labels' not in line:
                stock_data.append(line)

    date,closep,highp,lowp,openp,adjclosep,volume = np.loadtxt(stock_data,
                                                     delimiter=',',
                                                     unpack=True,
                                                     # %Y =full year 2015
                                                     # %y = partial year 15
                                                     # %m = number month
                                                     # %H number hours
                                                     # %M  number minutes
                                                     # %S number seconds
                                                     converters={0: mdates.bytespdate2num('%Y-%m-%d')})


    plt.plot_date(date,closep,'-',label='Price')


    plt.xlabel('Date')
    plt.ylabel('Price')

    plt.title('Lect 8+9')

    plt.legend()

    plt.show()

graph_stock()









# '''
#     1.
#     First, you
#     must
#     have
#     a
#     current
#     installation
#     of
#     pandas(check
#     version
#     with:
#         import pandas as pd, pd.__version__).
#     2.
#     Second, you
#     have
#     to
#     install
#     pandas_datareader(pip
#     install
#     pandas_datareader)
#     3.
#     Then, at
#     least if you
#     're running version 20.3, these lines will pull in the data:
#
#     from pandas_datareader import data, wb
#     df = data.DataReader('TSLA', 'yahoo')
#     df
#
#     My
#     finished
#     function(
#     for this module) looked like this, and I didn't have to do all the date manipulation:
#
#     def graph_data(stock):
#         df = data.DataReader(stock, 'yahoo')
#         plt.plot_date(df.index, df.Close, '-')
#
#         plt.xlabel('Date')
#         plt.ylabel('Price')
#         plt.title('Interesting Graph')
#         plt.legend()
#         plt.show()
#
#     graph_data('TSLA')
#
#     Hope
#     this
#     helps!
# '''