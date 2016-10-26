import os
import pandas
import matplotlib.pyplot as plt

"""
    path = "./Data/SENSEX/<SYMBOL>.csv"

"""
def get_max_close(path):
    """ returns the max closing value for the stock whose path has
        been supplied   """
    df = pandas.read_csv(path)
    return df['Close'].max()

def plot_values(path):
    df = pandas.read_csv(path)
    #print df['High'] beware of [[DOUBLE BRACKETS]] for multiple values
    df[['High', 'Adj Close']].plot()
    plt.show()

def get_mean_volume(path):
    """Returns the mean volume for stock
    """
    df = pandas.read_csv(path)
    return df['Volume'].mean()

def symbol_to_path(symbol, base_dir = "./Data/SENSEX"):
    """Returns CSV file path for given symbol """
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


"""def make_dataframe(path, start_date, end_date):
    dates = pandas.date_range(start_date, end_date)
    #This is an empty DataFrame which is indexed by Date
    df1 = pandas.DataFrame(index = dates)

    #ReadSPY data into temporary dataframe
    #indexes column by Date,, parse_dates = True allows the dataframe to be
    #be indexed as DateTime value objects,,
    dfSENSEX = pandas.read_csv(path, index_col = "Date", parse_dates = True)

    #now lets join the dataframes
    dfSENSEX = pandas.read_csv(path, index_col = "Date",parse_dates = True,
                        #usecols = ['Date', 'Adj Close'],
                        na_values = ['nan'])

    #dropna() drops any nan values and this join  is by default left join,
    #df1 = df1.join(dfSENSEX, how = 'inner')
    #df1 = df1.dropna()
    #print df1
    #reading more stocks

    symbols = ['TCS', 'ITC']
    for symbol in  symbols:
        df_temp = pandas.read_csv(symbol_to_path(symbol),
                               index_col = "Date", parse_dates = True,
                               usecols = ['Date', 'Adj Close'],na_values = ['nan'])

        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(df_temp, how = 'inner')
    print df1
"""

def get_data_frame(symbols, dates):

    df = pandas.DataFrame(index = dates)

    #sensex file acts as base;  this is the index file for sensex
    if 'SENSEX' not in symbols:
        symbols.insert(0, 'SENSEX')

    for symbol in  symbols:
        df_temp = pandas.read_csv(symbol_to_path(symbol),
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
    print df

def test_run():

    start_date = '2014-01-01'
    end_date = '2016-10-07'
    dates = pandas.date_range(start_date, end_date)
    symbols = ['TCS', 'ITC']
    get_data_frame(symbols, dates)


if __name__ == "__main__":
    test_run()