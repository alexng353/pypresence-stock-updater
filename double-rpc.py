from pypresence import Presence
import time, os, array, datetime, configparser
import yahoo_fin.stock_info as yahoo

#So it reads .ini files now

parser = configparser.ConfigParser()

parser.read("config2.ini")

client_id = parser['config']['clientID']

stonk = parser['stocks']['stock1']
stonk2 = parser['stocks']['stock2']


#client_id = f.readline
RPC = Presence(client_id) 
RPC.connect() 

#I'll fix it another day, I'm tired now.
#stonk = "eth-cad"
#stonk2  = "btc-cad"

def price(stockName):
    return round(yahoo.get_live_price(stockName), 3)

def updater():
    stock = price(stonk)
    stock2 = price(stonk2)
    RPC.update(details=f"1 {stonk2.upper()} = ${stock2}", state=f"1 {stonk.upper()} = ${stock}", large_image=f"{stonk2}", small_image=f"{stonk}", large_text=f"Displaying Live ${stonk.upper()} and ${stonk2.upper()} price", small_text=f"${stonk.upper()}", buttons=[{"label":"Updating every second", "url":"https://www.google.com/search?q=what+is+one+second"},{"label":"Made by alexng353","url":"https://github.com/alexng353-new/pypresence-stock-updater"}], )
    
while True:
    updater()
    print(f"\nUpdated price for ${stonk.upper()}: ${price(stonk)} | Updated price for ${stonk2.upper()}: ${price(stonk2)}     Time: {datetime.datetime.now()}")
    time.sleep(1)
