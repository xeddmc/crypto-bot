import urllib, json, time
import itertools
from itertools import count
from datetime import datetime
#Choose ID for market desired
ID = "3" #LTC/BTC
Coin ="LTC" #Ticker for Primary coin
url = "http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid="+ID

#Function to unpack JSON data, retrieve last trade price and time of trade
def unpack():
    response = urllib.urlopen(url);
    load = json.loads(response.read())
    #data = json.dumps(load, sort_keys=True, indent=4)
    
    return load
    pass

   
#Create Datafiles
#outfile=open('Data.txt','a')
orderfile=open('OpenOrders.txt', 'a')
tradesfile=open('RecentTrades.txt', 'a')


i=0
#Generator to take price readings every 2mins and write to file
while 1:
    try:
        dict={'LTC':3,'FTC': 5, 'NVC':13, 'NMC':29,'DOGE':132, 'DOGE':135}
        for ticker, iter in dict.iteritems():
            Coin = ticker
            ID = str(iter)
            url = "http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid="+ID
           
            new = unpack() #Call function to get JSON request
            
            #Get Data from JSON       
            a=new['return'].get('markets')
            price=a[Coin].get('lasttradeprice')
            primary=a[Coin].get('primarycode')
            secondary=a[Coin].get('secondarycode')
            volume= a[Coin].get('volume')
            dt=a[Coin].get('lasttradetime')
            d,t = dt.split( )
    
            #Get sytem date&time
            T=datetime.now()
            cdate, ctime = str(T)[0:19].split()
            
                       
                
            #Save Depth of market at given time
            buyorders=a[Coin].get('buyorders')
            for bdicts in buyorders:
                orderprice= str(bdicts['price'])
                orderquant= str(bdicts['quantity'])
                ordertotal= str(bdicts['total'])
                buystring = primary + '/' + secondary + '\t' +'Buy price'+ '\t' + orderprice + '\t' + 'Buy quantity' + '\t' + orderquant + '\t' + 'Buy total' + '\t' + ordertotal + '\n'
                orderfile.write(buystring)
            sellorders=a[Coin].get('sellorders')
            for sdicts in sellorders:
                orderprice= str(sdicts['price'])
                orderquant= str(sdicts['quantity'])
                ordertotal= str(sdicts['total'])
                sellstring = primary + '/' + secondary + '\t' + 'Sell price'+ '\t' + orderprice + '\t' + 'Sell quantity' + '\t' + orderquant + '\t' + 'Sell total' + '\t' + ordertotal +'\n'
                orderfile.write(sellstring)

            #Save data from last 100 Trades 
            recenttrades=a[Coin].get('recenttrades')
            for tdicts in recenttrades:
                tradeid   = str(tdicts['id'])
                tradeprice= str(tdicts['price'])
                tradequant= str(tdicts['quantity'])
                tradetotal= str(tdicts['total'])
                tradetime=  str(tdicts['time'])
                recentstring= primary + '/' + secondary + '\t' + tradeid + '\t' + tradetime + '\t'+'price'+ '\t' + price + '\t' + 'quantity' + '\t' + tradequant + '\t' + 'total' + '\t' + tradetotal + '\n'
                tradesfile.write(recentstring)
                print recentstring
            tradesfile.write('\n\n\n')
            orderfile.write('\n\n\n')
        time.sleep(300)

    except ValueError, AttributeError:
        print 'Sorry, trying again'
        for j in xrange(10):
            print j+1
            time.sleep(1)
        pass        