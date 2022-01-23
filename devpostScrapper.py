#imports
import requests
import pandas
from devpostEvent import getUrlEvent

class devpost:
    def __init__(self):
        self.pageNo = 1
        self.totalPage = 0

    def setUrlForEachPage(self):
        return 'https://devpost.com/api/hackathons?page={}&status[]=upcoming&status[]=open'.format(self.pageNo)

    def makeRequest(self):
        urlRecieve = self.setUrlForEachPage()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        request = requests.get(urlRecieve,headers = headers)
        return request

    def getJson(self):
        self.data = self.makeRequest().json()
    
    def numberOfEvents(self):
        self.getJson()
        totalEvents = self.data['meta']['total_count']
        eventsShowPerPage = self.data['meta']['per_page']
        self.totalPage = totalEvents//eventsShowPerPage if totalEvents%eventsShowPerPage == 0 else totalEvents//eventsShowPerPage+1
        

    def extractData(self):
        #declarations of lists
        self.eventTitle = []
        self.id=[]
        self.eventDate = []
        self.eventTimeLeft = []
        self.eventLocation = []
        self.eventState = []
        self.eventOrganizationName = []
        self.eventTheme = []
        self.eventRegisteredCount = []
        self.eventUrl = []
        self.eventEligible = []
        self.eventDescription = []
        self.eventStartDate = []
        self.eventEndDate = []
        
        while (self.pageNo<self.totalPage+1):
            self.getJson()
            for events in self.data['hackathons']:
                self.eventTitle.append(events['title'])
                self.id.append(events['id'])
                self.eventState.append(events['open_state'])
                self.eventDate.append(events['submission_period_dates'])
                date = events['submission_period_dates']
                length = len(date)
                if(length != 27):
                    year = date[-4:]
                    if(length == 12):
                        self.eventStartDate.append(date)
                        self.eventEndDate.append(date)
                    if(length == 17):
                        startDate = date[4:6]
                        endDate = date[9:11]
                        month = date[:3]
                        Startdates = month + ' ' + startDate + ', ' + year
                        Enddates = month + ' ' + endDate + ', ' + year
                        self.eventStartDate.append(Startdates)
                        self.eventEndDate.append(Enddates)
                    if(length == 21):
                        startDate = date[0:6]
                        endDate = date[9:15]
                        Startdates = startDate + ', ' + year
                        Enddates = endDate + ', ' + year
                        self.eventStartDate.append(Startdates)
                        self.eventEndDate.append(Enddates)
                else:
                    dates = date.split(' - ')
                    self.eventStartDate.append(dates[0])
                    self.eventEndDate.append(dates[1])
                self.eventTimeLeft.append(events['time_left_to_submission'])
                self.eventLocation.append(events['displayed_location']['location'])
                self.eventRegisteredCount.append(events['registrations_count'])
                self.eventUrl.append(events['url'])
                self.eventOrganizationName.append(events['organization_name'])
                themeTitle = []
                for theme in events['themes']:
                    themeTitle.append(theme['name'])
                self.eventTheme.append(themeTitle)  
                (eligible,description) = (getUrlEvent(events['url']))
                self.eventEligible.append(eligible)
                self.eventDescription.append(description)
            print("Page completed reading....{}".format(self.pageNo))    
            self.pageNo += 1  

            

        
    def dataToCsv(self):
        tableData = pandas.DataFrame(self.eventTitle,columns=['Name'])
        tableData['ID'] = self.id
        tableData['Event Start Date'] = self.eventStartDate
        tableData['Event End Date'] = self.eventEndDate
        tableData['Registration End date']=''
        tableData['Registration status'] = self.eventState
        tableData['Event Url'] = self.eventUrl
        #tableData['Time Left'] = self.eventTimeLeft
        
        #tableData['Theme'] = self.eventTheme
        #tableData['Registered Count'] = self.eventRegisteredCount
        #tableData['Event hosted by'] = self.eventOrganizationName
        tableData['Event Description'] = self.eventDescription
        tableData['Team Size'] = 'N/A'
        tableData['Name of the Website']='Devpost'
        return(tableData)
        
