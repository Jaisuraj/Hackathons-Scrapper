
import requests
import pandas as pd
import html2text

class DevFolio:

    def __init__(self):
        self.page = 0
        self.id=0
        self.data=[]

    def set_url(self):
        return f"https://api.devfolio.co/api/hackathons?filter={self.data[self.page]}&page=1&limit=20"
    def make_request(self):
        self.data=['application_open','upcoming','live']
        url= self.set_url()
        return requests.request("GET",url)
    def get_data(self):
        self.data= self.make_request().json()


    

    def Scrapper(self,pages):
        id=[]
        name = []
        start_date = []
        end_date = []
        reg_status = []
        teamsize=[]
        seo_url = []
        details = []
        i=0
        for page in range(1,pages+1):
            self.make_request()
            self.get_data()
            for item in self.data['result']:
                id.append(item['uuid'])
                name.append(item['name'])
                start_date.append(item['starts_at'][0:10])
                end_date.append(item['ends_at'][0:10])
                if(item['apply_mode']=='both'):
                    reg_status.append('Open')
                else:
                    reg_status.append('Upcoming')
                seo_url.append(item['hackathon_setting']['site'])
                details.append(html2text.html2text(item['desc']))
                teamsize.append(item['team_size'])

            self.page+=1


            
        df = pd.DataFrame(name, columns=['Name'])
        df['ID'] = id
        df['Event Start Date'] = start_date
        df['Event End Date'] = end_date
        df['Registration End date']=''
        df['Registration status'] = reg_status
        df['Event Url'] = seo_url
        df['Event Description']=details
        df['Team Size']=teamsize
        df['Name of the Website']='Devfolio'

        return(df)
   