import requests
import pandas
from bs4 import BeautifulSoup
from hackerearthhackathon import getUrlHackathon
from hackerearthchallenge import getUrlChallenge
from hackerearthrated import getUrlRated

def Hackerearth():
    url = "https://www.hackerearth.com/challenges/?filters=competitive%2Chackathon%2Cuniversity"
    request = requests.get(url).text

    soup = BeautifulSoup(request,"html5lib")

    challengeType = []
    challengeTitle = []
    challengeLink = []
    challengeEligible = []
    challengeIdeaStartDate = []
    challengeIdeaEndDate = []
    challengeIdeaLocation = []
    challengeHackStartDate = []
    challengeHackEndDate = []
    challengeHackLocation = []
    challengeDescription = []
    challengeDuration = []
    challengeStatus = []


    ongoingData = soup.find('div',attrs={'class':'ongoing challenge-list'})
    upcomingData = soup.find('div',attrs={'class':'upcoming challenge-list'})
    typeData = ongoingData.findAll(attrs={'class':'challenge-type'})
    upcomingTypeData = upcomingData.findAll('div',attrs={'class':'challenge-type'})
    titleData = ongoingData.findAll('span',attrs={'class':'challenge-list-title challenge-card-wrapper'})
    upcomingTitleData = upcomingData.findAll('span',attrs={'class':'challenge-list-title challenge-card-wrapper'})
    linkData = ongoingData.findAll('a',attrs={'class':'challenge-card-wrapper challenge-card-link'})
    upcomingLinkData = upcomingData.findAll('a',attrs={'class':'challenge-card-wrapper challenge-card-link'})

    for Type in typeData:
        challengeType.append((Type.text).strip())
        challengeStatus.append('Open')

    for uType in upcomingTypeData:
        challengeType.append((uType.text).strip()) 
        challengeStatus.append('Upcoming')   

    for title in titleData:
        challengeTitle.append(title.text)

    for uTitle in upcomingTitleData:
        challengeTitle.append(uTitle.text)

    for link in linkData:
        links = link.get('href')
        if(links[0:5] != 'https'):
            links = "https://www.hackerearth.com"+links
        challengeLink.append(links)

    for ulink in upcomingLinkData:
        links = ulink.get('href')
        if(links[0:5] != 'https'):
            links = "https://www.hackerearth.com"+links
        challengeLink.append(links)

    for (Type,Title,link) in zip(challengeType,challengeTitle,challengeLink):
        print("Reading...........")
        print(Type)
        print(Title)
        if(Type == 'HACKATHON'):
            teamSize,ideaStartDate,ideaEndDate,ideaLocation,hackStartDate,hackEndDate,hackLocation,description = (getUrlHackathon(link))
            teamSize = teamSize.replace('-','to')
            challengeEligible.append(teamSize)
            challengeIdeaStartDate.append(ideaStartDate)
            challengeIdeaEndDate.append(ideaEndDate)
            challengeIdeaLocation.append(ideaLocation)
            challengeHackStartDate.append(hackStartDate)
            challengeHackEndDate.append(hackEndDate)
            challengeHackLocation.append(hackLocation)
            challengeDescription.append(description)
            challengeDuration.append(None)
    
        if(Type == 'COMPETITIVE'):
            location,details,description = getUrlChallenge(link)
            challengeEligible.append(None)
            challengeIdeaStartDate.append(None)
            challengeIdeaEndDate.append(None)
            challengeIdeaLocation.append(None)
            challengeHackLocation.append(location)
            challengeHackStartDate.append(details[0])
            challengeHackEndDate.append(details[1])
            challengeDuration.append(details[2])
            challengeDescription.append(description)
        
        if(Type == 'RATED'):
            rateLoc,rateDetails,detail = (getUrlRated(link))
            challengeEligible.append(None)
            challengeIdeaLocation.append(None)
            challengeIdeaStartDate.append(None)
            challengeIdeaEndDate.append(None)
            challengeHackLocation.append(rateLoc)
            challengeHackStartDate.append(rateDetails[0])
            challengeHackEndDate.append(rateDetails[1])
            challengeDuration.append(rateDetails[2])
            challengeDescription.append(detail)

    print(challengeEligible)
    print(challengeTitle)

    table = pandas.DataFrame(challengeTitle,columns=['Name'])
    table['ID']=''
    table['Registration status']= challengeStatus
    #table['Event Type'] = challengeType
    #table['Idea Phase Location'] = challengeIdeaLocation
    table['Event Start Date'] = challengeHackStartDate
    table['Event End Date'] = challengeHackEndDate
    #table['Event Location'] = challengeHackLocation
    #table['Event Duration'] = challengeDuration
    table['Event Url'] = challengeLink
    table['Event Description'] = challengeDescription
    table['Team Size'] = challengeEligible
    table['Name of the Website']='Hackerearth'
    table['Idea Phase Start Date'] = challengeIdeaStartDate
    table['Idea Phase End Date'] = challengeIdeaEndDate
    return(table)

