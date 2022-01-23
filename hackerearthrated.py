from attr import attr
import requests
from bs4 import BeautifulSoup

def getUrlRated(url):
    request = requests.get(url).text

    soup = BeautifulSoup(request,'html5lib')

    rateLoc = soup.find('span',attrs={'class':'event-loc dark small standard-margin-right'})
    rateLoc = (rateLoc.text).strip()

    rateStartDate = soup.findAll('span',attrs={'class':'timing-text dark regular weight-700'})
    
    ratedDetails = []
    
    for info in rateStartDate:
        ratedDetails.append(info.text)

    overView = soup.find('div',attrs={'class':'section-desc regular dark'})
    
    detail = ''
    for overview in overView:
        detail += (overview.text)

    return (rateLoc,ratedDetails,detail)