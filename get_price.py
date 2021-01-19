from datetime import datetime, timedelta
import sys
import requests

if __name__ == "__main__":
    col = 5 # the column for the ISO timestamp
    for line in sys.stdin.readlines():
        start = datetime.fromisoformat(line.split(',')[col].strip())
        end = start + timedelta(minutes=10)
        resp = requests.get("https://api.pro.coinbase.com/products/AVAX-USD/candles?start={start}&end={end}&granularity=60".format(start=start.strftime('%Y-%m-%dT%H:%M:%SZ'), end=end.strftime('%Y-%m-%dT%H:%M:%SZ')))
        data = resp.json()
        ps = [(d[2]+d[1])/2 for d in data]
        if len(ps) == 0:
            resp = requests.get('https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=AVAX_USDT&from={start}&to={end}&interval=1m'.format(start=int(start.timestamp()), end=int(end.timestamp())))
            data = resp.json()
            ps = [(float(d[3])+float(d[4]))/2 for d in data]
        ts = [int(d[0]) for d in data]
        ts.sort()
        timestamps=(datetime.utcfromtimestamp(int(data[0][0])), datetime.utcfromtimestamp(int(data[-1][0])))
        print("{},{:2f},{},{}".format(line.strip(), sum(ps)/len(ps), timestamps[0].strftime('%Y-%m-%dT%H:%M:%SZ'), timestamps[1].strftime('%Y-%m-%dT%H:%M:%SZ')))
