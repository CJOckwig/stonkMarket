import requests
import datetime
import csv
import pandas as pd
from bs4 import BeautifulSoup as bs

# gets todays date to put in csv
date = datetime.date.today()

# makes list to store new row of data
TodaysData = []

# adds todays date to the first element of the list
TodaysData.append(date)

# reads first row of csv files
file = open('stocks.csv', 'r', newline='')
reader = csv.reader(file)
CsvHeaders = next(reader)

# gets amount of columns in csv
NumCol = len(CsvHeaders)
file.close()
# sets count to run while loop for every stock name in csv column header
Count = 1
while Count < NumCol:

    # gets page content for the google search of stock ticker
    StockWeb = requests.get("https://www.google.com/search?q="+ CsvHeaders[Count] +"+stock")
    pagecontent = StockWeb.content

    # uses bs4 to process and parse page code for certain tags
    pageparser = bs(pagecontent, 'html.parser')
    StockPrice = pageparser.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).get_text()

    # this loop formats the stock price text to get rid of excess chars after first space
    FormatedStockPrice = ""
    char_index = 0
    while char_index != -1:
        if StockPrice[char_index] == " ":
            char_index = -1
        else:
            FormatedStockPrice = (FormatedStockPrice + StockPrice[char_index])
            char_index = char_index + 1

    # this adds the stock price to the list of prices
    TodaysData.append(FormatedStockPrice)

    # prints notification to see what stock names have been added so far
    print("Added", CsvHeaders[Count], "stock to list.")

    #adds count for while loop
    Count = Count + 1

# Appends the csv file to add the new row of data
file = open('stocks.csv', 'a', newline="")
writer = csv.writer(file)
writer.writerow(TodaysData)
file.close()

# prints out data frame of stock data using pandas
StockData = pd.read_csv("stocks.csv")
print("\n\n", StockData)