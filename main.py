from d2c import *
from devfolio import *
from devpostScrapper import *
from hackerearth import *
import pandas as pd

scrapper= D2C()
scrapper1= DevFolio()
devpostScrap = devpost()
devpostScrap.makeRequest()
devpostScrap.numberOfEvents()
devpostScrap.extractData()
pd.concat([scrapper.Scrapper(4),scrapper1.Scrapper(3),devpostScrap.dataToCsv(),Hackerearth()]).to_csv('dataconcatf.csv', index=False)

