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

def make_dataframe(path):
    start_date = '2014-01-01'
    end_date = '2016-10-07'
    dates = pandas.date_range(start_date, end_date)
    #This is an empty DataFrame which is indexed by Date
    df1 = pandas.DataFrame(index = dates)

    #ReadSPY data into temporary dataframe
    #indexes column by Date,, parse_dates = True allows the dataframe to be
    #be indexed as DateTime value objects,,
    dfSENSEX = pandas.read_csv(path, index_col = "Date", parse_dates = True)

    #now lets join the dataframes
    dfSENSEX = pandas.read_csv(path, index_col = "Date",parse_dates = True,
                        usecols = ['Date', 'Adj Close'],
                        na_values = ['nan'])

    #dropna() drops any nan values and this join  is by default left join,
    df1 = df1.join(dfSENSEX)
    df1 = df1.dropna()
    print df1

def test_run():
    """ my driver function
    """
    path = "./Data/SENSEX/TCS.csv"
    make_dataframe(path)

    """for symbol in ['ITC' , 'TCS']:
        print "Max Close is"
        path = "./Data/SENSEX/{}.csv".format(symbol)
        #print symbol, get_mean_volume(path)
        plot_values(path)
    """

if __name__ == "__main__":
    test_run()