import urllib, json, time
import itertools
from itertools import count
#Choose ID for market desired
ID = "132" #DOGE/BTC
url = "http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid="+ID

#Function to unpack JSON data, retrieve last trade price and time of trade
def unpack():
    response = urllib.urlopen(url);
    load = json.loads(response.read())
    data = json.dumps(load, sort_keys=True, indent=4)
         #del load["buyorders"]
         #price = [p for p in load if load.find('last') ==1]
    print data
    return data
    pass

   
#Create Datafile
outfile=open('Data.txt','w')
outfile.write('Market \t Current Price \t' + str(time.localtime) + '\t \n')

#Generator to take price readings every 10s and write to file
while 1:
    new = unpack()
    outfile.write(new)
    

    time.sleep(10)
    print unpack()



