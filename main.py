import requests
import datetime
import csv
import pandas as pd

from bs4 import BeautifulSoup as bs


def main():
    # gets todays date to put in csv
    # adds todays date to the first element of the list
    # reads first row of csv files
    date = datetime.date.today()
    todaysData = []
    todaysData.append(date)


    tickList = []
    #findTickers(tickList)


    file = open('stocks.csv', 'r', newline='')
    reader = csv.reader(file)
    CsvHeaders = next(reader)

    # gets amount of columns in csv
    NumCol = len(CsvHeaders)
    file.close()
    # finished reading file-closes so we can append it later.





    ###############################################################
    # This loop will iterate equal to the amount of               #
    # columns in the stocks.csv file                              #
    # searches price and collects raw string which will look like #
    # 'currentVal +/-changeprice (%change)'                       #
    # formats down to just currentVal                             #
    ###############################################################


    count = 1
    while count < NumCol:
        price_nyse_unformatted = searchPrice(CsvHeaders[count])
        print(price_nyse_unformatted)
        price_nyse = formatPrice(price_nyse_unformatted)
        todaysData.append(price_nyse)
        print("Added", CsvHeaders[count], "stock to list.")
        count = count + 1
        # adds count for while loop (gg ez)

    writeToFile(todaysData)
    # prints out data frame of stock data using pandas
    stockData = pd.read_csv("stocks.csv")
    print("\n\n", stockData)


# Takes in ticker letter combo to search web URL
def searchPrice(ticker):
    stockWeb = requests.get("https://www.google.com/search?q=" + ticker + "+stock")

    if stockWeb.status_code == 200:
        pageContent = stockWeb.content
        # uses bs4 to process and parse page code for certain tags
        pageParser = bs(pageContent, 'html.parser')
        try:
            stockPrice = pageParser.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).get_text()
        except:
            stockPrice =" "
    return stockPrice

def formatPrice(base):
    formatedStockPrice = ""
    char_index = 0
    while char_index != -1:
        if base[char_index] == " ":
            char_index = -1
        else:
            formatedStockPrice = (formatedStockPrice + base[char_index])
            char_index = char_index + 1
    return formatedStockPrice

def writeToFile(todaysData):
    # Appends the csv file to add the new row of data

    file = open('stocks.csv', 'a', newline="")
    writer = csv.writer(file)
    writer.writerow(todaysData)
    file.close()

def findTickers(tickList):
    data = pd.read_csv("tickers.csv")
    tickList = data["Ticker"].to_list()
    print(tickList)
    file = open("stocks.csv", 'w')
    write = csv.writer(file)
    write.writerow(tickList)
    file.close()




main()
