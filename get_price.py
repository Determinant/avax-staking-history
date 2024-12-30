from datetime import datetime, timedelta
import sys
import requests

if __name__ == "__main__":
    col = 5 # the column for the ISO timestamp
    for line in sys.stdin.readlines():
        start = datetime.fromisoformat(line.split(',')[col].strip())
        end = start + timedelta(minutes=10)
        resp = requests.get("https://api.exchange.coinbase.com/products/AVAX-USD/candles?start={start}&end={end}&granularity=60".format(start=start.strftime('%Y-%m-%dT%H:%M:%SZ'), end=end.strftime('%Y-%m-%dT%H:%M:%SZ')))
        data = resp.json()
        ps = [(d[2]+d[1])/2 for d in data]
        if len(ps) == 0:
            resp = requests.get('https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=AVAX_USDT&from={start}&to={end}&interval=1m'.format(start=int(start.timestamp()), end=int(end.timestamp())))
            data = resp.json()
            if 'label' not in data:
                ps = [(float(d[3])+float(d[4]))/2 for d in data]
        #ts = [int(d[0]) for d in data]
        #ts.sort()
        timestamps=("-", "-")
        if len(ps) > 0:
            timestamps=(datetime.utcfromtimestamp(int(data[0][0])).strftime('%Y-%m-%dT%H:%M:%SZ'), datetime.utcfromtimestamp(int(data[-1][0])).strftime('%Y-%m-%dT%H:%M:%SZ'))
        print("{},{},{},{}".format(line.strip(), "{:2f}".format(sum(ps)/len(ps)) if len(ps) > 0 else "", timestamps[0], timestamps[1]))
