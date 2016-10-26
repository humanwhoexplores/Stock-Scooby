import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path = "./Data/SENSEX/<SYMBOL>.csv"

def symbol_to_path(symbol, base_dir = "./Data/SENSEX"):
    """Returns CSV file path for given symbol """
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data_frame(symbols, dates):

    df = pd.DataFrame(index = dates)

    #sensex file acts as base;  this is the index file for sensex
    if 'SENSEX' not in symbols:
        symbols.insert(0, 'SENSEX')

    for symbol in  symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol),
                               index_col = "Date", parse_dates = True,
                               usecols = ['Date', 'Adj Close'],na_values = ['nan'])

        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        if symbol != 'SENSEX':
            df = df.join(df_temp)
        else:
            df = df.join(df_temp, how = 'inner')
        """
            This is important as SENSEX csv file is base for all stocks
             we have an entry for this whenever SENSEX trades,
             but for any compamy listed on sensex, it may not trade for all
             days sensex has worked,, so we take a left join
        """
    return df

def normalize_data(df):
    #normalize using first row of data
    #observe use of row slicing
    return df/df.ix[0,:]

def plot_data(df, theTitle = "Stock Prices"):
    """plot stock prices """
    df = normalize_data(df)
    ax = df.plot(title = theTitle)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    #df[['ITC', 'TCS']].plot(title = theTitle)
    plt.show()

def compute_stats(df):
    print "the standard deviation is \n", df.std()
    print "the mean is\n", df.mean()

def compute_bollinger_bands(df, length=30, numsd=2):
    """ returns average, upper band, and lower band
        there are three steps , find rolling mean, then rolling std deviation
        then find upper and lower bands
    """
    rm = pd.stats.moments.rolling_mean(df,length)
    rmstd = pd.stats.moments.rolling_std(df,length)
    upperband = rm + (rmstd*numsd)
    lowerband = rm - (rmstd*numsd)
    #plotting these stats
    ax  = df['TCS'].plot(title = "Bollinger Bands", label = "TCS")
    rm.plot(label = "Rolling mean", ax = ax)
    upperband.plot(label='upper band', ax = ax)
    lowerband.plot(label = 'lower band ', ax = ax)
    plt.show()

def compute_daily_returns(df):
    daily = df.copy()
    daily[1:] = (df[1:] / df[:-1].values) - 1
    #hey using values only for second is necessary bcoz
    # else it will do index wise stuff, so our goal os shifting
    #by 1 and dividing is destroyed,
    daily.ix[0, :] = 0
    print "the cumulative returns \n", daily.sum()

def test_run():

    start_date = '2014-01-01'
    end_date = '2016-10-07'
    dates = pd.date_range(start_date, end_date)
    symbols = ['SENSEX']
    df = get_data_frame(symbols, dates)
    #plot_data(df)

    #compute_bollinger_bands(df, 20, 2)
    compute_daily_returns(df)

if __name__ == "__main__":
    test_run()