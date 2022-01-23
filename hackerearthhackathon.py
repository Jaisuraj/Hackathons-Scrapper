import requests
from bs4 import BeautifulSoup

def getUrlHackathon(url):
    request = requests.get(url).text

    soup = BeautifulSoup(request,'html.parser',from_encoding='utf-8')

    teamSize = soup.find('strong')
    teamSize = (teamSize.text).strip()

    try:
        ideaPhase = soup.find('div',attrs={'class':'idea-phase time-location-specification'})
        ideaStart = ideaPhase.find('div',attrs={'class':'start-time-block'})
        ideaEnd = ideaPhase.find('div',attrs={'class':'end-time-block'})
        ideaLocation = ideaPhase.find('div',attrs={'class':'location-block'})
        ideaStartDate = ideaStart.find('div',attrs={'class':'regular bold desc dark'})
        ideaEndDate = ideaEnd.find('div',attrs={'class':'regular bold desc dark'})
        iLocation = ideaLocation.find('div',attrs={'class':'regular bold desc dark'})
        ideaStartDate = (ideaStartDate.text).strip()
        ideaEndDate = (ideaEndDate.text).strip()
        iLocation = (iLocation.text).strip()
    except:
        ideaStartDate = None
        ideaEndDate = None
        iLocation = None

    hackPhase = soup.find('div',attrs={'class':'hack-phase time-location-specification'})
    hackStart = hackPhase.find('div',attrs={'class':'start-time-block'})
    hackEnd = hackPhase.find('div',attrs={'class':'end-time-block'})
    hackLocation = hackPhase.find('div',attrs={'class':'location-block'})
    hackStartDate = hackStart.find('div',{'class':'regular bold desc dark'})
    hackEndDate = hackEnd.find('div',attrs={'class':'regular bold desc dark'})
    hLocation = hackLocation.find('div',attrs={'class':'regular bold desc dark'})
    hackStartDate = (hackStartDate.text).strip()
    hackEndDate = (hackEndDate.text).strip()
    hLocation = (hLocation.text).strip()

    details = soup.find('div',attrs={'class':'content'})

    description = ''
    for detail in details:
        description += (detail.text)

    return (teamSize,ideaStartDate,ideaEndDate,iLocation,hackStartDate,hackEndDate,hLocation,description)  