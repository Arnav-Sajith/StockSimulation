import yfinance as yf
import time

tsla = yf.Ticker("TSLA")

old_price = 0
price = tsla.info['currentPrice']
wallet = 1000
daily_trade_gain = []



def buy():
    while True:
        if time.gmtime().tm_hour <= 19:
            first_price = tsla.info['currentPrice']
            time.sleep(60)
            current_price = tsla.info['currentPrice']


            difference = (current_price - first_price) / first_price
            if difference > 0.01:
                return tsla.info['currentPrice']
            
def sell(bought_price):
    while True:
        current_price = tsla.info['currentPrice']
        
        if time.gmtime().tm_hour >= 23:
            return tsla.info['currentPrice']

        if bought_price < current_price * 1.001: 
            return tsla.info['currentPrice']
            



while True:
    buy_price = buy()
    sell_price = sell(buy_price)
    difference = (sell_price - buy_price) / buy_price
    daily_trade_gain.append(difference)
