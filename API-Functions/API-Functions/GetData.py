import urllib, json, time
import itertools
from itertools import count
#Choose ID for market desired
ID = "3" #LTC/BTC
Coin ="LTC" 
url = "http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid="+ID

#Function to unpack JSON data, retrieve last trade price and time of trade
def unpack():
    response = urllib.urlopen(url);
    load = json.loads(response.read())
    data = json.dumps(load, sort_keys=True, indent=4)
    
    return load
    pass

   
#Create Datafile
outfile=open('Data.txt','w')
outfile.write('Market \t Current Price \t' + str(time.localtime) + '\t \n')

#Generator to take price readings every 30s and write to file
while 1:
    new = unpack()
    a=new['return'].get('markets')
    price=a[Coin].get('lasttradeprice')
    outfile=open('Data.txt', 'a')
    outfile.write(price + '\n')
    
    
    time.sleep(30)
    print price


