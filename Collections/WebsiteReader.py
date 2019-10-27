from bs4 import BeautifulSoup
import requests

class WebsiteReader():

    page_content = ''

    def __init__(self, url):
        self.__url = url

    def getUrl(self):
        return self.__url

    def setUrl(self, url):
        self.__url = url

    def getHtml(self):
        page = requests.get(self.__url)
        self.page_content = page.content
        soup = BeautifulSoup(self.page_content, 'html.parser')
        output = soup.prettify()
        return output

    def htmlSeperatorByID(self, id):
        output = []
        soup = BeautifulSoup(self.page_content, 'html.parser')
        event_month = soup.find(id=id)
        return event_month