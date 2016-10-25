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

def plot_high_values(path):
    df = pandas.read_csv(path)
    print df['High']
    df['High'].plot()
    plt.show()

def test_run():
    """ my driver function """
    for symbol in ['ITC' , 'TCS']:
        print "Max Close is"
        path = "./Data/SENSEX/{}.csv".format(symbol)
        print symbol, get_max_close(path)

if __name__ == "__main__":
    test_run()