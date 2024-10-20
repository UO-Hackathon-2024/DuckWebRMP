'''
#uncomment everything and it should work, i was missing some reliant libraries and don't want to install

import time
import schedule

from dw_to_database import main as dw_main
from rmp_scraper import main as rmp_main


def dw_scraper():
    print('Running Duckweb Scraper')
    dw_main()
    
    rmp_scraper()


def rmp_scraper():
    print('Running Rate My Professor Scraper')
    rmp_main()


schedule.every(24).hours.do(dw_scraper)

while True:
    schedule.run_pending()
    time.sleep(10)
'''