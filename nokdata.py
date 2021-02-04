import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup as bs

# requests access to webpage
nok = requests.get("https://www.google.com/finance/quote/NOK:NYSE?sa=X&ved=2ahUKEwiq0_-T_87uAhWSK80KHe1lDBkQ3ecFMAB6BAgCEBE")

# status code
#print(nok.status_code)

nokia = (nok.content)
soup = bs(nokia, 'html.parser')

time = datetime.datetime.now()
print("\nCurrent time: ",time, "\n")

sf = pd.read_csv('stonks.csv')
print("Stonks data:\n" ,sf)


def searchprice():
    price = soup.find('div', {'class': 'YMlKec fxKbKc'}).get_text()
    #print(price)
    nok_stonk = float(price[1:])
    f_n_s = format(nok_stonk, '.2f')
    print("\nThe current NOK stock price is:", f_n_s)
    if (nok_stonk > 5.5):
        print("\nsell stock")
    else:
        print("\nHold you paper hand bitch!!!")



searchprice()


