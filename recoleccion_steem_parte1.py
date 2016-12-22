# -*- coding: utf-8 -*-
    
import json
import datetime

data_file= open('STEEM_2016.json')   
data = json.load(data_file)
data_history = data['history']
    

for todos_los_dias in data_history:
                #if "07" in todos_los_dias[3:]:
    
                    precio_dia = data_history[todos_los_dias]['price']
                    en_dolar = precio_dia['usd']
                    en_BTC = precio_dia['btc']
                    en_jpy = precio_dia['jpy']
                    
                    
                    poscion = data_history[todos_los_dias]['position']
                    print  'A la Fecha ', todos_los_dias, 'Los Precios son;'
                    print   "                                       en Dolares:  ", en_dolar
                    print   "                                       en Bitcoins:  " ,en_BTC 
                    print   "                                       en Yenes:  " ,en_jpy 
                    