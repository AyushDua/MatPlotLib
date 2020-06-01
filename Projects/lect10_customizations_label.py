import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import urllib.request


def graph_stock():

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))



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

                                                     converters={0: mdates.bytespdate2num('%Y-%m-%d')})


    ax1.plot_date(date,closep,'-',label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.grid(True)#,color='g',linestyle='-')


    plt.xlabel('Date')
    plt.ylabel('Price')

    plt.title('Lect 10')

    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.18,right=0.94,top=0.90,wspace=0.2,hspace=0)
    plt.show()

graph_stock()









