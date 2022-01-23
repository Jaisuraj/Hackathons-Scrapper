
import requests
import pandas as pd
import html2text

class D2C:

    def __init__(self):
        self.page = 1
        self.id=0

    def set_url(self):
        return f"https://dare2compete.com/api/public/opportunity/search-new?opportunity=hackathons&sort=&dir=&filters=Open&types=oppstatus&atype=explore&page={self.page}&showOlderResultForSearch=false"
    def make_request(self):
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
        rem = []
        seo_url = []
        details = []
        teamsize = []
        i=0
        for page in range(1,pages+1):
            self.make_request()
            self.get_data()
            for item in self.data['data']['data']:
                id.append(item['id'])
                name.append(item['title'])
                start_date.append(item['start_date'][0:10])
                end_date.append(item['end_date'][0:10])
                if(item['regnRequirements']['reg_status']=='STARTED'):
                    reg_status.append('Open')
                else:
                    reg_status.append('Upcoming')
                rem.append(item['regnRequirements']['remain_days'])
                seo_url.append(item['seo_url'])
                self.id=id
                data2 =requests.request("GET",f"https://dare2compete.com/api/public/competition/{id[i]}").json()
                details.append((html2text.html2text(data2['data']['competition']['details'])))
                teamsize.append((data2['data']['competition']['regnRequirements']['max_team_size']))
                i=i+1

                
                
                #print("Name:",name,"Start date:",start_date[0:10], "End Date:", end_date[0:10],"Registration Status:", reg_status,"Remaining Days: ",rem,"URL:", seo_url)

            self.page += 1
        df = pd.DataFrame(name, columns=['Name'])
        df['ID'] = id
        df['Event Start Date'] = start_date
        df['Event End Date'] = end_date
        df['Registration End date']=''
        df['Registration status'] = reg_status
        #df['Remaining Days'] = rem
        df['Event Url'] = seo_url
        df['Event Description']=details
        df['Team Size']=teamsize
        #df['Event Duration']='N/A'
        df['Name of the Website']='D2C'
        return(df)


