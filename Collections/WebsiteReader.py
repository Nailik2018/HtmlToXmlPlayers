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

    def getHtml2(self):
        page = requests.get(self.__url)
        self.page_content = page.content
        soup = BeautifulSoup(self.page_content, 'html.parser')
        output = soup.prettify()
        return output

    def getHtml(self):
        url = self.__url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        output = []

        result_of_player = soup.find_all(class_="border-light-light-gray-bottom")
        i = 0

        for single in result_of_player:

            elo_of_victim = single.
            print(elo_of_victim)

            if "td" in single:
                print("JAAAAAAAAAa")
            else:
                print("--------")
                #print(single)

            i += 1

        print(result_of_player[1])

        return output

    def htmlSeperatorByID(self, id):
        output = []
        soup = BeautifulSoup(self.page_content, 'html.parser')
        event_month = soup.find(id=id)
        return event_month