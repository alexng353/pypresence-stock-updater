from pypresence import Presence
import time, os, array, datetime
import yahoo_fin.stock_info as yahoo

f = open("config.txt", "r")

client_id = f #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

stonk = "eth-cad"
stonk2  = "btc-cad"

def price(stockName):
    return round(yahoo.get_live_price(stockName), 3)

def updater():
    stock = price(stonk)
    stock2 = price(stonk2)
    RPC.update(details=f"1 {stonk2.upper()} = ${stock2}", state=f"1 {stonk.upper()} = ${stock}", large_image=f"{stonk2}", small_image=f"{stonk}", large_text=f"Displaying Live ${stonk.upper()} and ${stonk2.upper()} price", small_text=f"${stonk.upper()}", buttons=[{"label":"Data from Yahoo Finance", "url":f"https://ca.finance.yahoo.com/quote/{stonk.upper()}/"},{"label":"Updating every 1 second","url":f"https://ca.finance.yahoo.com/quote/{stonk2.upper()}/"}], )
    
while True:
    updater()
    print(f"\nUpdated price for ${stonk.upper()}: ${price(stonk)} | Updated price for ${stonk2.upper()}: ${price(stonk2)}     Time: {datetime.datetime.now()}")
    time.sleep(1)
