
from nsepy import get_history
from datetime import date
from matplotlib import pyplot

## URL --> https://3cgnyk66sd.execute-api.ap-south-1.amazonaws.com/dev

def nse_py(name):
    data = get_history(symbol="SBIN", start=date(2020, 9, 9), end=date(2020, 9, 9))
    print(data)

#    pyplot.plot(data[["Close"]])
#    pyplot.show()


if __name__ == '__main__':
    nse_py(__name__)
