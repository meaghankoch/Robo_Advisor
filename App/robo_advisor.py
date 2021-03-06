from dotenv import load_dotenv
import os

load_dotenv() #> loads contents of the .env file into the script's environment

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
#print(ALPHAVANTAGE_API_KEY)


import requests
import json
import csv

import datetime
t = datetime.datetime.now()

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
symbol = "IBM" 
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(request_url)
#print(type(response)) --> requests.models.Response'
#print(response.status_code) #--> 200
#print(response.text)



def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71





#changing data to dict from str
parsed_response = json.loads(response.text)




#Data Investigation
#print(type(parsed_response))
#print(parsed_response.keys())
#print(parsed_response["Meta Data"])
#print(parsed_response["Time Series (Daily)"])
# print(parsed_response)
#print(parsed_response["Meta Data"].keys())
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
#print(last_refreshed)

#latest_close = parsed_response["Time Series (Daily)"]["2020-06-11"]["4. close"]
#print(latest_close)

tsd = parsed_response["Time Series (Daily)"]
#print(type(tsd.keys())) --> Dict_Keys
#list(tsd.keys())

date_keys = tsd.keys()
dates = list(date_keys) # TO DO: assumes first day is on top, but need to ensure latest day is on top
latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

usd_latest_close = (float(tsd[latest_day]["4. close"])) #changing latest close to float

#maximum of all high prices
#recent_high = max(high_prices) 

high_prices = []

for date in dates: 
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices)


low_prices = []

for date in dates: 
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_low = min(low_prices)



def recco(): # NOTE: the trailing parentheses are required
    if usd_latest_close < recent_high:
        return("BUY!")
    else:
        return("DO NOT BUY!")

def reason(): 
    if recco =="BUY!":
        return("Because stock is undervalued")
    else: 
        return("Because stock is undervalued")

zs = []
while True: 
    z = input("Please input the IBM Stock Symbol:")
    if z == "IBM" or z == "ibm" or z == "iBM":
        break 
    elif z != "IBM":
        print("Hey, are you sure that stock symbol is correct? Please try again!")

    else:
         zs.append(z)


csv_file_path = "data/prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above


    for date in dates: 
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"], 
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
    })





# app/robo_advisor.py

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", str((t.strftime("%Y-%m-%d"))), str(t.strftime("%I:%M %p")))
print("-------------------------")
print(f"LATEST DAY:{last_refreshed}")
print(f"LATEST CLOSE:{to_usd(float(latest_close))}")
print(f"RECENT HIGH:{to_usd(float(recent_high))}")
print(f"RECENT LOW:{to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {recco()}")
print(f"RECOMMENDATION REASON:{reason()}")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


