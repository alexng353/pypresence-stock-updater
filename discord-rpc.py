from pypresence import Presence
import time, os, array, datetime
import yahoo_fin.stock_info as yahoo

f = open("config.txt", "r")

client_id = f #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

stonk = "eth-cad"

def price(stockName):
    return round(yahoo.get_live_price(stockName), 3)

def updater(stonkName):
    stock = price(stonkName)
    RPC.update(state="Updating every second", details=f"1 {stonkName.upper()} = ${stock}" , large_image="stonk", small_image=f"{stonkName}", large_text=f"Displaying Live ${stonkName.upper()} price", small_text=f"${stonkName.upper()}", buttons=[{"label": f"{stonkName.upper()} on Yahoo", "url":f"https://ca.finance.yahoo.com/quote/{stonkName.upper()}/"}])
    
while True:
    updater(stonk)
    print(f"\nUpdated price for ${stonk.upper()}: ${price(stonk)}     Time: {datetime.datetime.now()}")
    time.sleep(1)
