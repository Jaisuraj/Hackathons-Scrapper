import requests
from bs4 import BeautifulSoup

def getUrlChallenge(url):
    request = requests.get(url).text
    soup = BeautifulSoup(request,'html5lib')

    challengeLocation = soup.find('span',attrs={'class':'event-loc dark small standard-margin-right'})
    challengeLocation = (challengeLocation.text).strip()

    challenge = soup.findAll('span',attrs={'class':'timing-text dark regular weight-700'})
    competitiveDetails = []
    for i in challenge:
        competitiveDetails.append(i.text)
    
    challengeDetails = soup.find('div',attrs={'class':'section-desc regular dark'})
    description = ''
    for detail in challengeDetails:
        description += (detail.text)

    return (challengeLocation,competitiveDetails,description)