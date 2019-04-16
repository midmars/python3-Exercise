#-*-coding: UTF=8-*-

def download():
    import csv
    import requests
    # CSV_URL = 'http://www.aec.gov.tw/open/gammamonitor.csv'
    CSV_URL='http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=csv'
    # /od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=csv
    with requests.Session() as s:
        download = s.get(CSV_URL)
        download = download.content
        cr = csv.reader(download.splitlines(), delimiter=',')
        my_list = list(cr)
        with open("gammadata.csv", "a") as fp:
            wr = csv.writer(fp)
            for line in my_list:
                wr.writerow(line[1:])   
import time
from datetime import datetime
while True:
    download()
    print("Dowloaded at:",str(datetime.now()))
    time.sleep(10*60)