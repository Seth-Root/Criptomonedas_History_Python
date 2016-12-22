# -*- coding: utf-8 -*-
# -*- decoding: utf-8 -*-
    
import json  
import datetime 

from operator import itemgetter 



import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import os
os.system("rm STEEM_2016.json")

os.system("wget http://coinmarketcap.northpole.ro/api/v5/history/STEEM_2016.json")

data_file= open('STEEM_2016.json')   
data = json.load(data_file)  
data_history = data['history']
    
dict_days = {}  
list_in_BTC = []
list_in_dolar = []
list_dict_days = []
for all_days in data_history:   
                    prices_day = data_history[all_days]['price']
                    in_dolar = prices_day['usd']
                    list_in_dolar.append(in_dolar)
                    in_BTC = prices_day['btc']
                    list_in_BTC.append(in_BTC)
                    all_days = datetime.datetime.strptime(all_days,'%d-%m-%Y')
                    dict_days = {'usd':in_dolar, 'date': all_days, 'btc': in_BTC}
                    list_dict_days.append(dict_days)










n_dict = sorted( list_dict_days, key = itemgetter('date') ,reverse=True)

iterer = 0
print "                "
print "               Value STEEM in 10 Days"
print "                "
last_10_days_prices = []
last_10_days_dates = []
for dict_dia_a_dia in n_dict:
  if iterer < 10:
         print "Value in Dolares: ", dict_dia_a_dia['usd'], "in Date: ",dict_dia_a_dia['date'].date()
         iterer += 1
         last_10_days_prices.append(dict_dia_a_dia['usd'])
         day = dict_dia_a_dia['date']
         day = day.strftime('%Y-%m-%d')
         last_10_days_dates.append(day)




print "                "
print "              Minimum Value STEEM in Date"
print "                "



dict_min_usd = min( list_dict_days, key = itemgetter('usd') )
print "Value in Dolares:", dict_min_usd['usd'], "in Date: ",     dict_min_usd['date'].date()

print "                "
print "              Maximum Value STEEM in Date"
print "                "
dict_max_usd = max( list_dict_days, key = itemgetter('usd') )
print "Value in Dolares:", dict_max_usd['usd'], "in Date: ",dict_max_usd['date'].date()







list_minimos = sorted( list_dict_days, key = itemgetter('usd') ,reverse=True)

list_max = sorted( list_dict_days, key = itemgetter('usd') ,reverse=False)


iterer = 0
print "                "
print "  10 Maximum Values del STEEM in Dates"
print "                "
for dict_dia_a_dia in list_minimos:
   if iterer < 10:
      print "Value in Dolares:", dict_dia_a_dia['usd'], "in Date: ",     dict_dia_a_dia['date'].date()
      iterer += 1


iterer = 0
print "                "
print "  10 Minimum Values del STEEM in Dates"
print "                "
for dict_dia_a_dia in list_max:
   if iterer < 10:
      print "Value in Dolares:", dict_dia_a_dia['usd'], "in Date: ",     dict_dia_a_dia['date'].date()
      iterer += 1




dates = last_10_days_dates
print dates
x = [datetime.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
y = last_10_days_prices # many thanks to Kyss Tao for setting me straight here


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
plt.gcf().autofmt_xdate()

plt.show()



iterer = 0
print "                "
print "               Value STEEM in 30 Days"
print "                "
last_30_days_prices = []
last_30_days_dates = []
for dict_dia_a_dia in n_dict:
  if iterer < 30:
         print "Value in Dolares: ", dict_dia_a_dia['usd'], "in Date: ",dict_dia_a_dia['date'].date()
         iterer += 1
         last_30_days_prices.append(dict_dia_a_dia['usd'])
         day = dict_dia_a_dia['date']
         day = day.strftime('%Y-%m-%d')
         last_30_days_dates.append(day)




dates = last_30_days_dates
print dates
x = [datetime.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
y = last_30_days_prices # many thanks to Kyss Tao for setting me straight here


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
plt.gcf().autofmt_xdate()

plt.show()









