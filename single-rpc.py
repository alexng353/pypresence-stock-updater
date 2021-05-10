from pypresence import Presence
import time, os, array, datetime, configparser
import yahoo_fin.stock_info as yahoo


#config reader
parser = configparser.ConfigParser()
parser.read("config.ini")

client_id = parser['config']['clientID']
stonk = parser['stocks']['stock1']

#connect to discord rich presence application
RPC = Presence(client_id) 
RPC.connect()

#unoptimized spaghetti code
def price(stockName):
    return round(yahoo.get_live_price(stockName), 3)

def updater(stonkName):
    stock = price(stonkName)
    RPC.update(state="Updating every second", details=f"1 {stonkName.upper()} = ${stock}" , large_image="stonk", small_image=f"{stonkName}", large_text=f"Displaying Live ${stonkName.upper()} price", small_text=f"${stonkName.upper()}", buttons=[{"label": "Updating every second", "url":"https://www.google.com/search?q=what+is+one+second"},{"label":"Made by alexng353","url":"https://github.com/alexng353-new/pypresence-stock-updater"}])
    
while True:
    updater(stonk)
    print(f"\nUpdated price for ${stonk.upper()}: ${price(stonk)}     Time: {datetime.datetime.now()}")
    time.sleep(1)
