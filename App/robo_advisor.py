from dotenv import load_dotenv
import os

load_dotenv() #> loads contents of the .env file into the script's environment

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
print(ALPHAVANTAGE_API_KEY)


import requests
import json



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
print(last_refreshed)

latest_close = parsed_response["Time Series (Daily)"]["2020-06-11"]["4. close"]
print(latest_close)




#Info inputs




# app/robo_advisor.py

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:" )
print("-------------------------")
print(f"LATEST DAY:{last_refreshed}")
print(f"LATEST CLOSE:{to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



