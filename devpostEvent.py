from urllib import request
import requests
from bs4 import BeautifulSoup

def getUrlEvent(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    request = requests.get(url,headers = headers).text

    soup = BeautifulSoup(request,'html.parser',from_encoding='utf-8')

    eligible = soup.find('ul',attrs={'id':'eligibility-list'})
    eligible = (eligible.text).strip()

    description = soup.find('article',attrs={'id':'challenge-description'})
    description = (description.text).strip()

    return(eligible,description)