import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup as bs

# requests access to webpage
nok = requests.get("https://www.google.com/finance/quote/NOK:NYSE?sa=X&ved=2ahUKEwiq0_-T_87uAhWSK80KHe1lDBkQ3ecFMAB6BAgCEBE")

# status code
#print(nok.status_code)

# stores page content in var nokia
nokia = (nok.content)
# parses and processes page content using bs4
soup = bs(nokia, 'html.parser')

# uses datetime to print the current time
time = datetime.datetime.now()
print("\nCurrent time: ",time, "\n")

# reads csv using pandas and prints it
sf = pd.read_csv('stonks.csv')
print("Stonks data:\n" ,sf)

# this function searches for the price of the nokia stock
def searchprice():

    # searches for the html code responsible for nok price and gets the text
    price = soup.find('div', {'class': 'YMlKec fxKbKc'}).get_text()
    #print(price)
    # turns the text from string to float and formats out the $
    nok_stonk = float(price[1:])
    # formats the stock price to 2 decimal places
    f_n_s = format(nok_stonk, '.2f')
    # prints the current formated stock price (the formatted price is a string)
    print("\nThe current NOK stock price is:", f_n_s)
    # prints statement based on price (this variable is un-formatted but is a float type)
    if (nok_stonk > 5.5):
        print("\nsell stock")
    else:
        print("\nHold you paper hand retard!!!")


# calls the search price function
searchprice()


