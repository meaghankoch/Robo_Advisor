from dotenv import load_dotenv
import os

load_dotenv() #> loads contents of the .env file into the script's environment

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
print(ALPHAVANTAGE_API_KEY)


import requests
import json
import csv



request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
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



csv_file_path = "data/prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above

    writer.writerow({
        "timestamp": "To Do",
        "open":"To Do",
        "high": "To Do",
        "low": "To Do", 
        "close": "To Do",
        "volume": "To Do"
    })










# app/robo_advisor.py

print("-------------------------")
print("SELECTED SYMBOL: IBM")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:" )
print("-------------------------")
print(f"LATEST DAY:{last_refreshed}")
print(f"LATEST CLOSE:{to_usd(float(latest_close))}")
print(f"RECENT HIGH:{to_usd(float(recent_high))}")
print(f"RECENT LOW:{to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


